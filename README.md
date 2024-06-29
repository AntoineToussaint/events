Some notes:

* I wanted to go wide rather than deep. The particularity of 3rd party integrations is not something I spent any time on.

* What I wanted is to show how to setup the base of system that is easily testable and maintainable, showcasing best practices, from using `pydantic`, `fastapi`, type annotation, `async`, etc...

* I wrote the base of a system where it's easy to add new 3rd party searches efficiently by leveraging `asyncio` primitives.

* I focused a lot on testing from the HTTP side to search aggregation also most of it is WIP.
```chatinput
 codefly test service api
Running <api>
⚠️ A new version of codefly is available. Please update to v0.0.110
vendelux/api >> starting execution environment in native mode
vendelux/api >> will run on http://localhost:18342
vendelux/api >> testing poetry app
vendelux/api >> ============================= test session starts ==============================
vendelux/api >> platform darwin -- Python 3.10.13, pytest-8.2.2, pluggy-1.5.0 -- /Users/antoine/Library/Caches/pypoetry/virtualenvs/server-Eszva6xZ-py3.10/bin/python
vendelux/api >> cachedir: .pytest_cache
vendelux/api >> rootdir: /Users/antoine/Development/jobs/vendelux/services/api/code
vendelux/api >> configfile: pyproject.toml
vendelux/api >> plugins: asyncio-0.23.7, anyio-4.4.0
vendelux/api >> asyncio: mode=strict
vendelux/api >> collecting ... Starting server
vendelux/api >> collected 4 items
vendelux/api >> 
vendelux/api >> tests/events/test_collector.py::test_collector PASSED
vendelux/api >> tests/events/test_events.py::test_events PASSED
vendelux/api >> tests/test_app.py::test_version PASSED
vendelux/api >> tests/test_app.py::test_mock_search PASSED
vendelux/api >> 
vendelux/api >> ============================== 4 passed in 1.20s ===============================
Stopping services

```

* I used codefly to get a few things out of the box:
  - python fastapi + poetry
  - openAPI schema (auto generated) at `services/api/openapi`
  - Docker
  - Kubernetes

This is the main reason why there is no documentation on how to run, test, build or deploy. `codefly` takes care of that.

**Local run**
```chatinput
 codefly run service api
Running <api>
⚠️ A new version of codefly is available. Please update to v0.0.110
vendelux/api >> starting execution environment in native mode
vendelux/api >> will run on http://localhost:18342
vendelux/api >> starting poetry app
vendelux/api >> INFO:     Will watch for changes in these directories: ['/Users/antoine/Development/jobs/vendelux/services/api/code']
vendelux/api >> INFO:     Uvicorn running on http://0.0.0.0:18342 (Press CTRL+C to quit)
vendelux/api >> INFO:     Started reloader process [4303] using StatReload
vendelux/api >> Starting server
vendelux/api >> runtime mode
vendelux/api >> INFO:     Started server process [4307]
vendelux/api >> INFO:     Waiting for application startup.
vendelux/api >> INFO:     Application startup complete.
vendelux/api >> INFO:     127.0.0.1:49419 - "POST /events/search HTTP/1.1" 200 OK

```

```chatinput
❯ curl -X POST http://0.0.0.0:18342/events/search
{"events":[{"name":"Event(0)","start":null,"end":null},{"name":"Event(1)","start":null,"end":null},{"name":"Event(2)","start":null,"end":null},{"name":"Event(3)","start":null,"end":null},{"name":"Event(4)","start":null,"end":null},{"name":"Event(5)","start":null,"end":null},{"name":"Event(6)","start":null,"end":null},{"name":"Event(7)","start":null,"end":null},{"name":"Event(8)","start":null,"end":null},{"name":"Event(9)","start":null,"end":null}]}%   
```

**Kubernetes**

```chatinput
(DEBUG) (resources.NewFlatLayout) create root=/Users/antoine/Development/jobs/vendelux
(DEBUG) (provider.Load) loaded services svcs=vendelux/api
(DEBUG) (provider.Load) adding service conf
(DEBUG) (providers.Load) loaded dns=
(DEBUG) (exposeService) k8s namespace=vendelux-localkube service=svc/api
exposing vendelux/api at http://localhost:18342
^C%                                                                                                                                                                                                                
❯ vim .gitignore
❯ k get po
NAME                   READY   STATUS    RESTARTS   AGE
api-6f599c6787-xzm8c   1/1     Running   0          3m9s

```

* Code is `services/api/code/src` and testing is in `services/api/code/tests`.

* I didn't spent any time looking at the actual 3rd party APIs:
  - Eventbrite, the first one I looked at deprecated their API
  - Meetup seems to have moved full time to GraphQL

Since it's supposed to be fun, I focused on getting a generic way to add Search components with `async`.
