from app.mcp.client import (
    DeliveryMCPClient
)


class CommunicationAgent:

    name = "CommunicationAgent"

    async def execute(
        self,
        client: DeliveryMCPClient
    ):

        stakeholders = (
            await client.read_resource(
                "stakeholder://contacts"
            )
        )

        draft = await client.call_tool(
            "draft_status_update"
        )

        return {
            "stakeholders": stakeholders,
            "communication": draft
        }
