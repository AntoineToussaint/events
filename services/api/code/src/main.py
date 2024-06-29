from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import codefly_sdk.codefly as codefly
from src.models import *
from src.events.collector import Collector
from src.setup import setup

print("Starting server")

codefly.init()

app = FastAPI()

# if codefly.is_local():
origins = [
    "*",
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

collector = Collector()

if codefly.in_runtime_mode():
    print("runtime mode")
    searches = setup()
    for search in searches:
        collector.add(search)


@app.get("/version")
async def version():
    return {"version": codefly.get_version()}

@app.post("/events/search", response_model=EventSearchResponse)
async def events_search(req: Optional[EventSearchRequest] = None):
    events = await collector.get(req)
    return EventSearchResponse(events=events)
