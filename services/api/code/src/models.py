from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime


class EventSearchRequest(BaseModel):
    start: Optional[datetime] = None
    end: Optional[datetime] = None


class Event(BaseModel):
    name: str
    start: Optional[datetime] = None
    end: Optional[datetime] = None

class EventSearchResponse(BaseModel):
    events: List[Event]