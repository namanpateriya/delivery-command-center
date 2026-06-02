from app.mcp.client import (
    DeliveryMCPClient
)


class DeliveryAgent:

    name = "DeliveryAgent"

    async def execute(
        self,
        client: DeliveryMCPClient
    ):

        try:

            status = (
                await client.read_resource(
                    "project://status"
                )
            )

            summary = (
                await client.call_tool(
                    "generate_project_summary"
                )
            )

            return {

                "success": True,

                "project_status":
                status,

                "project_summary":
                summary
            }

        except Exception as e:

            return {

                "success": False,

                "error": str(e)
            }
