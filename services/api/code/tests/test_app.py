import os, sys
import pytest
from httpx import AsyncClient, ASGITransport
import time
import json

import codefly_sdk.codefly as codefly
from codefly_cli.codefly import with_dependencies, with_cli_logs, with_debug, with_code_path, with_silent

sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), '..'))

from src.main import app, collector
from src.events.search import Search
from src.models import *

with_cli_logs()
with_debug()
with_code_path(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))

@pytest.mark.asyncio
async def test_version():
    async with AsyncClient(transport=ASGITransport(app=app), base_url="http://localhost:8080") as ac:
        response = await ac.get("/version")
    assert response.status_code == 200
    assert response.json() == {"version": codefly.get_version()}



class MockSearch(Search):
    def __init__(self, up, to):
        self.up = up
        self.to = to

    async def get(self, req):
        return [Event(name=f"Event({i})") for i in range(self.up, self.to)]

@pytest.mark.asyncio
async def test_mock_search():
    # Do it once only, parsing JSON suck, test at business level!
    collector.add(MockSearch(0, 1))
    async with AsyncClient(transport=ASGITransport(app=app), base_url="http://localhost:8080") as ac:
        response = await ac.post("/events/search")
    assert response.status_code == 200
    expected = [Event(name="Event(0)")]
    got = [Event(**event_) for event_ in response.json()["events"]]
    assert expected == got