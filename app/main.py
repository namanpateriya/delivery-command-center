from fastapi import FastAPI

from app.schemas import (
    QueryRequest
)

from app.orchestrator.service import (
    DeliveryCommandCenter
)


app = FastAPI(
    title="Delivery Command Center",
    description=(
        "MCP-powered AI Delivery Copilot"
    ),
    version="1.0.0"
)


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

    result = await service.execute(
        request.query
    )

    return result
