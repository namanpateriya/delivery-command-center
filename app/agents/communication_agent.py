from app.config import (
    STAKEHOLDER_DATA_FILE
)

from app.utils.json_loader import (
    load_json_file
)

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

            logger.info(
                (
                    "Starting stakeholder "
                    "communication analysis"
                )
            )

            if client:

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

            else:

                stakeholders = (
                    load_json_file(
                        STAKEHOLDER_DATA_FILE
                    )
                )

                draft = {
                    "fallback": True,
                    "source": "json"
                }

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
                analysis,

                "stakeholders":
                stakeholders
            }

        except Exception as e:

            logger.exception(
                (
                    "Communication agent "
                    "failed"
                )
            )

            return {

                "success": False,

                "error": str(e)
            }
