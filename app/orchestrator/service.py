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

        client = (
            DeliveryMCPClient()
        )

        await client.connect()

        try:

            tasks = []

            for item in plan:

                agent = (
                    self.router.get_agent(
                        item
                    )
                )

                tasks.append(
                    agent.execute(
                        client
                    )
                )

            results = (
                await asyncio.gather(
                    *tasks
                )
            )

            return (
                self.aggregator.aggregate(
                    plan,
                    results
                )
            )

        finally:

            await client.close()
