from mcp import ClientSession

from mcp.client.stdio import (
    stdio_client,
    StdioServerParameters
)


class DeliveryMCPClient:

    def __init__(self):

        self.session = None
        self.transport = None

    def _normalize(
        self,
        response
    ):

        if hasattr(
            response,
            "content"
        ):
            return response.content

        return response

    async def connect(self):

        server_params = (
            StdioServerParameters(
                command="python",
                args=[
                    "-m",
                    "app.mcp.server"
                ]
            )
        )

        self.transport = (
            stdio_client(
                server_params
            )
        )

        read_stream, write_stream = (
            await self.transport.__aenter__()
        )

        self.session = ClientSession(
            read_stream,
            write_stream
        )

        await self.session.initialize()

    async def list_resources(self):

        return await (
            self.session.list_resources()
        )

    async def read_resource(
        self,
        uri: str
    ):

        response = (
            await self.session.read_resource(
                uri
            )
        )

        return self._normalize(
            response
        )

    async def list_tools(self):

        return await (
            self.session.list_tools()
        )

    async def call_tool(
        self,
        tool_name: str,
        arguments: dict | None = None
    ):

        arguments = arguments or {}

        response = (
            await self.session.call_tool(
                tool_name,
                arguments
            )
        )

        return self._normalize(
            response
        )

    async def close(self):

        if self.transport:

            await self.transport.__aexit__(
                None,
                None,
                None
            )
