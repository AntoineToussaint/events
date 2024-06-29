import os, sys
import pytest
from httpx import AsyncClient, ASGITransport
import time



import codefly_sdk.codefly as codefly
from codefly_cli.codefly import with_dependencies, with_cli_logs, with_debug, with_code_path, with_silent

sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), '../..'))

from src.models import EventSearchRequest, Event
from src.events.collector import deduplicate

@pytest.mark.asyncio
async def test_events():
    event = Event(name="hello")