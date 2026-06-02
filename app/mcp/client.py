from mcp import ClientSession

from mcp.client.stdio import (
    stdio_client,
    StdioServerParameters
)

from app.utils.logger import (
    get_logger
)

logger = get_logger(__name__)


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

        logger.info(
            "Connecting to MCP server"
        )

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

        logger.info(
            "MCP initialized"
        )

    async def discover_resources(self):

        resources = (
            await self.session.list_resources()
        )

        return self._normalize(
            resources
        )

    async def discover_tools(self):

        tools = (
            await self.session.list_tools()
        )

        return self._normalize(
            tools
        )

    async def read_resource(
        self,
        uri: str
    ):

        logger.info(
            f"Reading resource {uri}"
        )

        response = (
            await self.session.read_resource(
                uri
            )
        )

        return self._normalize(
            response
        )

    async def call_tool(
        self,
        tool_name: str,
        arguments=None
    ):

        arguments = arguments or {}

        logger.info(
            f"Calling tool {tool_name}"
        )

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

        logger.info(
            "Closing MCP session"
        )

        if self.transport:

            await self.transport.__aexit__(
                None,
                None,
                None
            )
