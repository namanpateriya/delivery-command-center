from app.mcp.client import (
    DeliveryMCPClient
)


class RiskAgent:

    name = "RiskAgent"

    async def execute(
        self,
        client: DeliveryMCPClient
    ):

        risks = await client.read_resource(
            "risk://open"
        )

        assessment = await client.call_tool(
            "assess_project_risk"
        )

        return {
            "risks": risks,
            "risk_assessment": assessment
        }
