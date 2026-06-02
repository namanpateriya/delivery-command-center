from app.mcp.client import (
    DeliveryMCPClient
)


class RiskAgent:

    name = "RiskAgent"

    async def execute(
        self,
        client: DeliveryMCPClient
    ):

        try:

            risks = (
                await client.read_resource(
                    "risk://open"
                )
            )

            assessment = (
                await client.call_tool(
                    "assess_project_risk"
                )
            )

            return {

                "success": True,

                "risks": risks,

                "risk_assessment":
                assessment
            }

        except Exception as e:

            return {

                "success": False,

                "error": str(e)
            }
