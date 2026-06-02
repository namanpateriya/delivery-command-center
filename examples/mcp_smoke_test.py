import asyncio

from app.mcp.client import (
    DeliveryMCPClient
)


async def main():

    client = (
        DeliveryMCPClient()
    )

    await client.connect()

    resources = (
        await client.discover_resources()
    )

    tools = (
        await client.discover_tools()
    )

    print(resources)

    print(tools)

    await client.close()


if __name__ == "__main__":

    asyncio.run(main())
