import asyncio

from app.orchestrator.service import (
    DeliveryCommandCenter
)


async def run():

    service = (
        DeliveryCommandCenter()
    )

    result = await service.execute(
        (
            "Project is delayed by "
            "3 weeks. Prepare "
            "leadership update."
        )
    )

    print(result)


if __name__ == "__main__":

    asyncio.run(run())
