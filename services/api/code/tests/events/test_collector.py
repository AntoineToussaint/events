import os, sys
import pytest
from httpx import AsyncClient, ASGITransport
import time



import codefly_sdk.codefly as codefly
from codefly_cli.ci import with_dependencies, with_cli_logs, with_debug, with_code_path, with_silent

sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), '../..'))

from src.main import app
from src.models import EventSearchRequest, Event
from src.events.search import Search
from src.events.collector import Collector

with_cli_logs()
with_debug()
with_code_path(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))

class MockSearch(Search):
    def __init__(self, up, to):
        self.up = up
        self.to = to

    async def get(self, req):
        return [Event(name=f"Event({i})") for i in range(self.up, self.to)]


@pytest.mark.asyncio
async def test_collector():
    c = Collector()
    c.add(MockSearch(0, 1))
    results = await c.get(None)
    assert results == [Event(name="Event(0)")]
