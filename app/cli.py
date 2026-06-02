import argparse
import asyncio
import json

from app.orchestrator.service import (
    DeliveryCommandCenter
)


async def execute_query(
    query: str
):

    service = (
        DeliveryCommandCenter()
    )

    result = await service.execute(
        query
    )

    print(
        "\n=== DELIVERY COMMAND CENTER ===\n"
    )

    print(
        json.dumps(
            result,
            indent=2,
            default=str
        )
    )


def main():

    parser = argparse.ArgumentParser(
        description=(
            "Delivery Command Center CLI"
        )
    )

    parser.add_argument(
        "--query",
        required=True,
        help=(
            "Program management query"
        )
    )

    args = parser.parse_args()

    asyncio.run(
        execute_query(
            args.query
        )
    )


if __name__ == "__main__":

    main()
