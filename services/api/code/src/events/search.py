from abc import ABC, abstractmethod
from typing import List
from src.models import EventSearchRequest, Event

class Search(ABC):
    @abstractmethod
    async def get(self, request: EventSearchRequest) -> List[Event]:
        pass