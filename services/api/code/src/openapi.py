import sys, os; sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))

import json
import codefly_sdk.codefly as codefly
from fastapi.openapi.utils import get_openapi

from src.main import app

if __name__ == "__main__":
    service = codefly.load_service_configuration()
    openapi_schema = get_openapi(
        title=service.name,
        version=service.version,
        routes=app.routes,
    )
    app.openapi_schema = openapi_schema
    openapi = app.openapi()
    with open("../openapi/api.swagger.json", "w") as f:
        f.write(json.dumps(openapi))
