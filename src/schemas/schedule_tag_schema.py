from pydantic import BaseModel


class ScheduleTagCreateRequest(BaseModel):
    name: str
    description: str

