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

from app.utils.logger import (
    get_logger
)

logger = get_logger(__name__)


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

        logger.info(
            (
                "Processing query: "
                f"{user_query}"
            )
        )

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

            for task_name in plan:

                agent = (
                    self.router.get_agent(
                        task_name
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
                    user_query,
                    plan,
                    results
                )
            )

        finally:

            await client.close()
