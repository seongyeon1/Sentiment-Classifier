from pydantic import BaseModel

class TextRequest(BaseModel):
    text: str

class TextResponse(BaseModel):
    label: str
    score: float
