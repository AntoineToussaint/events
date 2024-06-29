import asyncio
from typing import List, Iterable

from src.events.search import Search
from src.models import EventSearchRequest, Event

class Collector(Search):
    def __init__(self):
        self.searches = []

    def add(self, search: Search):
        self.searches.append(search)

    async def get(self, request: EventSearchRequest) -> List[Event]:
        tasks = [search.get(request) for search in self.searches]
        results = await asyncio.gather(*tasks)
        return deduplicate(results)

def deduplicate(groups: Iterable[List[Event]]) -> List[Event]:
    uniques = {}
    results = []
    for group in groups:
        for event in group:
            if event.name in uniques:
                continue
            results.append(event)
            uniques[event.name] = True
    return results


