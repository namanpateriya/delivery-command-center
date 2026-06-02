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
                analysis
            }

        except Exception as e:

            logger.exception(
                "Risk agent failed"
            )

            return {

                "success": False,

                "error": str(e)
            }
