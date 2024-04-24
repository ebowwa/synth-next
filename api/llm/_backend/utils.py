# api/llm/_backend/utils.py
import os
from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException
import logging
from typing import Tuple

def load_env_vars(app: FastAPI) -> None:
    load_dotenv()

def get_env_vars() -> Tuple[str, str]:
    agentops_api_key = os.getenv('AGENTOPS_API_KEY')
    mindsdb_api_key = os.getenv('MINDSDB_API_KEY')
    if not agentops_api_key or not mindsdb_api_key:
        logging.error("Environment variables not set")
        raise HTTPException(status_code=500, detail="Environment variables not set")
    return agentops_api_key, mindsdb_api_key