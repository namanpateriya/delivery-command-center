from app.mcp.client import (
    DeliveryMCPClient
)


class CommunicationAgent:

    name = "CommunicationAgent"

    async def execute(
        self,
        client: DeliveryMCPClient
    ):

        try:

            stakeholders = (
                await client.read_resource(
                    "stakeholder://contacts"
                )
            )

            draft = (
                await client.call_tool(
                    "draft_status_update"
                )
            )

            return {

                "success": True,

                "stakeholders":
                stakeholders,

                "communication":
                draft
            }

        except Exception as e:

            return {

                "success": False,

                "error": str(e)
            }
