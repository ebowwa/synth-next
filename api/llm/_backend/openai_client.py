
from openai import OpenAI, OpenAIError
from .models import ToolEvent, ErrorEvent, record
from fastapi import HTTPException
import logging

def create_openai_client(mindsdb_api_key: str) -> OpenAI:
    try:
        return OpenAI(api_key=mindsdb_api_key, base_url="https://llm.mdb.ai")
    except Exception as e:
        logging.error(f"Error creating OpenAI client: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Error creating OpenAI client: {str(e)}")

def get_openai_completion(openai_client: OpenAI, prompt: str, model: str, temperature: float, max_tokens: int, top_p: float, frequency_penalty: float, presence_penalty: float) -> dict:
    tool_event = ToolEvent(name='OpenAI Completion', params={'prompt': prompt, 'model': model, 'temperature': temperature, 'max_tokens': max_tokens, 'top_p': top_p, 'frequency_penalty': frequency_penalty, 'presence_penalty': presence_penalty})
    try:
        completion = openai_client.chat.completions.create(
            model=model,
            messages=[{"role": "user", "content": prompt}],
            temperature=temperature,
            max_tokens=max_tokens,
            top_p=top_p,
            frequency_penalty=frequency_penalty,
            presence_penalty=presence_penalty
        )
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