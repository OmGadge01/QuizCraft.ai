from pydantic import BaseModel


class GenerateTestResponse(BaseModel):
    response: str