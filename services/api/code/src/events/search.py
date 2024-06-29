from abc import ABC, abstractmethod
from typing import List
from src.models import EventSearchRequest, Event

class Search(ABC):
    """
    Generic Search class

    TODO: first improvement should be a non abstract class to handle time out
    and use this one from the collector
    """
    @abstractmethod
    async def get(self, request: EventSearchRequest) -> List[Event]:
        pass