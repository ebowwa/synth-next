# api/llm/_backend/models.py
from pydantic import BaseModel, Field
from typing import Tuple, Dict, Any
from agentops import record

class TextGenerationRequest(BaseModel):
    prompt: str
    model: str = "claude-3-haiku"
    temperature: float = 1.0
    max_tokens: int = 50
    top_p: float = 1.0
    frequency_penalty: float = 0.0
    presence_penalty: float = 0.0

class ToolEvent(BaseModel):
    name: str = Field(description="The name of the tool event")
    params: Dict[str, Any] = Field(description="The parameters used for the tool event")
    returns: str = Field(description="The result of the tool event")

class ErrorEvent(BaseModel):
    message: str
    trigger_event: ToolEvent