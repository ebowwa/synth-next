# api/llm/route.py
# [DEV/LOCAL] http://localhost:8000/{endpoints}
from typing import Tuple
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from openai import OpenAI, OpenAIError
from agentops import ToolEvent, ErrorEvent, record, init, start_session, end_session
import time
import os
from dotenv import load_dotenv
from pydantic import BaseModel, __version__ as pydantic_version

app: FastAPI = FastAPI()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Set up logging
import logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s: %(message)s')

@app.on_event("startup")
def load_env_vars() -> None:
    load_dotenv()

def get_env_vars() -> Tuple[str, str]:
    agentops_api_key: str = os.getenv('AGENTOPS_API_KEY')
    mindsdb_api_key: str = os.getenv('MINDSDB_API_KEY')
    if not agentops_api_key or not mindsdb_api_key:
        logging.error("Environment variables not set")
        raise HTTPException(status_code=500, detail="Environment variables not set")
    return agentops_api_key, mindsdb_api_key

def create_openai_client(mindsdb_api_key: str) -> OpenAI:
    try:
        return OpenAI(api_key=mindsdb_api_key, base_url="https://llm.mdb.ai")
    except Exception as e:
        logging.error(f"Error creating OpenAI client: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Error creating OpenAI client: {str(e)}")

def start_agentops_session(agentops_api_key: str) -> None:
    try:
        init(agentops_api_key)
        start_session()
    except Exception as e:
        logging.error(f"Error starting AgentOps session: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Error starting AgentOps session: {str(e)}")

def end_agentops_session(agentops_api_key: str, status: str) -> None:
    try:
        end_session(status)
    except Exception as e:
        logging.error(f"Error ending AgentOps session: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Error ending AgentOps session: {str(e)}")

class TextGenerationRequest(BaseModel):
    prompt: str

@app.post("/generate_text")
def generate_text(request: TextGenerationRequest) -> dict:
    try:
        agentops_key, mindsdb_key = get_env_vars()
        openai_client: OpenAI = create_openai_client(mindsdb_key)
        start_agentops_session(agentops_key)
        start_time: float = time.time()
        completion: dict = get_openai_completion(openai_client, request.prompt)
        end_time: float = time.time()
        duration: float = end_time - start_time
        logging.info(f"Ping: {duration:.2f} seconds")
        end_agentops_session(agentops_key, 'Success')
        return {"result": completion.choices[0].message.content}
    except HTTPException as e:
        end_agentops_session(agentops_key, 'Failure')
        raise e
    except Exception as e:
        end_agentops_session(agentops_key, 'Failure')
        logging.error(f"Unexpected error: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Unexpected error: {str(e)}")

def get_openai_completion(openai_client: OpenAI, prompt: str) -> dict:
    tool_event: ToolEvent = ToolEvent(name='OpenAI Completion', params={'prompt': prompt})
    try:
        completion: dict = openai_client.chat.completions.create(model="claude-3-haiku", messages=[{"role": "user", "content": prompt}])
        tool_event.returns = completion.choices[0].message.content
    except OpenAIError as e:
        logging.error(f"Error generating text: {str(e)}")
        record(ErrorEvent(message=str(e), trigger_event=tool_event))
        raise HTTPException(status_code=500, detail=f"Error generating text: {str(e)}")
    except Exception as e:
        logging.error(f"Unexpected error generating text: {str(e)}")
        record(ErrorEvent(message=str(e), trigger_event=tool_event))
        raise HTTPException(status_code=500, detail=f"Unexpected error generating text: {str(e)}")
    record(tool_event)
    return completion