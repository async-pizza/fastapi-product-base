import logging

from fastapi import FastAPI

from app.routes import app as routes

logging.basicConfig(level=logging.INFO)

app = FastAPI(docs_url="/api/swagger/", openapi_url="/api/openapi.json")
app.include_router(routes)


@app.get("/health/")
def health() -> str:
    return "i'm alive"
