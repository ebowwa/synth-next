# api/llm/index.py
# [DEV/LOCAL] http://localhost:8000/{endpoints}
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from ._backend.openai_client import get_openai_completion
from ._backend.agentops import start_agentops_session, end_agentops_session
from ._backend.utils import load_env_vars, get_env_vars
from ._backend.models import TextGenerationRequest
import time
import logging

app = FastAPI()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s: %(message)s')

# Load environment variables
load_env_vars(app)

@app.post("/generate_text")
def generate_text(request: TextGenerationRequest) -> dict:
    try:
        agentops_key, mindsdb_key = get_env_vars()
        start_agentops_session(agentops_key)
        start_time = time.time()
        completion = get_openai_completion(
            mindsdb_key,
            request.prompt,
            request.model,
            request.temperature,
            request.max_tokens,
            request.top_p,
            request.frequency_penalty,
            request.presence_penalty
        )
        end_time = time.time()
        duration = end_time - start_time
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

@app.get("/")
def ping() -> dict:
    return {"message": "Pong!"}