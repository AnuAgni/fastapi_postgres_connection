#This file supplies the basemodel using pydantic which is used by fastapi to post
from typing import TypeVar,Optional,Generic,List
from pydantic import BaseModel,Field

T=TypeVar('T')
class StudentInput(BaseModel):
    id:Optional[int]=None
    name:Optional[str]=None

    class Config:
        from_attributes=True


class RequestStudent(BaseModel):
    parameter: StudentInput = Field(...)

class Response(BaseModel, Generic[T]):
    code:str
    status: str
    message: str
    result:Optional[T]