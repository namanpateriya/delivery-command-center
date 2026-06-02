from app.config import (
    RISK_DATA_FILE
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


class RiskAgent:

    name = "RiskAgent"

    async def execute(
        self,
        client
    ):

        try:

            logger.info(
                "Starting risk analysis"
            )

            if client:

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

            else:

                risks = (
                    load_json_file(
                        RISK_DATA_FILE
                    )
                )

                assessment = {
                    "fallback": True,
                    "source": "json"
                }

            engine = (
                ReasoningEngine()
            )

            analysis = (
                await engine.analyze_risk(
                    {
                        "risks":
                        risks,

                        "assessment":
                        assessment
                    }
                )
            )

            return {

                "success": True,

                "analysis":
                analysis,

                "risks":
                risks
            }

        except Exception as e:

            logger.exception(
                "Risk agent failed"
            )

            return {

                "success": False,

                "error": str(e)
            }
