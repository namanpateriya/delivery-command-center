import asyncio

from app.config import (
    ENABLE_MCP
)

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

        client = None

        if ENABLE_MCP:

            client = (
                DeliveryMCPClient()
            )

            try:

                await client.connect()

                logger.info(
                    "MCP connection established"
                )

            except Exception:

                logger.exception(
                    (
                        "MCP unavailable. "
                        "Using fallback mode."
                    )
                )

                client = None

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

            if client:

                await client.close()
