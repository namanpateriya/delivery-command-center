import asyncio

from app.mcp.client import (
    DeliveryMCPClient
)

from app.orchestrator.planner import (
    WorkflowPlanner
)

from app.orchestrator.router import (
    AgentRouter
)

from app.orchestrator.aggregator import (
    ResultAggregator
)


class DeliveryCommandCenter:

    def __init__(self):

        self.planner = (
            WorkflowPlanner()
        )

        self.router = (
            AgentRouter()
        )

        self.aggregator = (
            ResultAggregator()
        )

    async def execute(
        self,
        user_query: str
    ):

        plan = (
            self.planner.create_plan(
                user_query
            )
        )

        client = DeliveryMCPClient()

        await client.connect()

        try:

            delivery_agent = (
                self.router.get_agent(
                    "delivery"
                )
            )

            risk_agent = (
                self.router.get_agent(
                    "risk"
                )
            )

            communication_agent = (
                self.router.get_agent(
                    "communication"
                )
            )

            delivery_result = (
                await delivery_agent.execute(
                    client
                )
            )

            risk_result = (
                await risk_agent.execute(
                    client
                )
            )

            communication_result = (
                await communication_agent.execute(
                    client
                )
            )

            return (
                self.aggregator.aggregate(
                    delivery_result,
                    risk_result,
                    communication_result
                )
            )

        finally:

            await client.close()
