from fastapi import FastAPI

from pydantic import BaseModel

from app.orchestrator.service import (
    DeliveryCommandCenter
)


app = FastAPI(
    title="Delivery Command Center",
    version="1.0.0"
)


class QueryRequest(
    BaseModel
):

    query: str


@app.get("/")
async def health():

    return {
        "status": "healthy",
        "service":
        "delivery-command-center"
    }


@app.post("/analyze")
async def analyze(
    request: QueryRequest
):

    service = (
        DeliveryCommandCenter()
    )

    return await service.execute(
        request.query
    )
