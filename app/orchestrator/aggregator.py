from app.llm.reasoning_engine import (
    ReasoningEngine
)

from app.utils.logger import (
    get_logger
)

logger = get_logger(__name__)


class CommunicationAgent:

    name = "CommunicationAgent"

    async def execute(
        self,
        client
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

            engine = (
                ReasoningEngine()
            )

            analysis = (
                await engine.generate_communication(
                    {
                        "stakeholders":
                        stakeholders,

                        "draft":
                        draft
                    }
                )
            )

            return {

                "success": True,

                "analysis":
                analysis
            }

        except Exception as e:

            logger.exception(
                "Communication agent failed"
            )

            return {

                "success": False,

                "error": str(e)
            }
