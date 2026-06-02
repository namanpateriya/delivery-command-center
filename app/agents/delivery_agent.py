from app.llm.reasoning_engine import (
    ReasoningEngine
)

from app.utils.logger import (
    get_logger
)

logger = get_logger(__name__)


class DeliveryAgent:

    name = "DeliveryAgent"

    async def execute(
        self,
        client
    ):

        try:

            logger.info(
                "Starting delivery analysis"
            )

            resources = (
                await client.discover_resources()
            )

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

            engine = (
                ReasoningEngine()
            )

            analysis = (
                await engine.analyze_delivery(
                    {
                        "resources":
                        resources,

                        "status":
                        status,

                        "summary":
                        summary
                    }
                )
            )

            return {

                "success": True,

                "analysis":
                analysis,

                "project_status":
                status
            }

        except Exception as e:

            logger.exception(
                "Delivery agent failed"
            )

            return {

                "success": False,

                "error": str(e)
            }
