from abc import ABC, abstractmethod
from typing import List

import os

import codefly_sdk.codefly as codefly

from src.models import EventSearchRequest, Event
from src.events.search import Search

class Eventbrite(Search):
    def __init__(self):
        token = codefly.secret(service="api", name="eventbrite", key="TOKEN")
        if not token:
            raise Exception("no token found for eventbrite")
        self.token = token
    async def get(self, request: EventSearchRequest) -> List[Event]:
        # Seems the API for event search is deprecated
        # Use httpx for async request
        return []