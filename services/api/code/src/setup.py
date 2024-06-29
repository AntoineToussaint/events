from typing import Optional

from src.events.search import Search
# Add all the stuff you want
from src.events.eventbrite import Eventbrite
from src.models import *

class MockSearch(Search):
    def __init__(self, up, to):
        self.up = up
        self.to = to

    async def get(self, req):
        return [Event(name=f"Event({i})") for i in range(self.up, self.to)]

def setup() -> List[Search]:
    return [Eventbrite(), MockSearch(0, 10)]
