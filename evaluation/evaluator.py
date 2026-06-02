import asyncio

from app.orchestrator.service import (
    DeliveryCommandCenter
)


class WorkflowEvaluator:

    async def evaluate(self):

        service = (
            DeliveryCommandCenter()
        )

        result = (
            await service.execute(
                (
                    "Project delayed by "
                    "3 weeks."
                )
            )
        )

        tests = []

        tests.append({
            "test": "workflow_execution",
            "passed": result is not None
        })

        tests.append({
            "test": "summary_present",
            "passed": (
                "executive_summary"
                in result
            )
        })

        tests.append({
            "test": "delivery_output",
            "passed": (
                "delivery"
                in result[
                    "executive_summary"
                ]
            )
        })

        tests.append({
            "test": "risk_output",
            "passed": (
                "risk"
                in result[
                    "executive_summary"
                ]
            )
        })

        tests.append({
            "test": "communication_output",
            "passed": (
                "communication"
                in result[
                    "executive_summary"
                ]
            )
        })

        return tests


async def main():

    evaluator = (
        WorkflowEvaluator()
    )

    results = (
        await evaluator.evaluate()
    )

    print(
        "\n=== EVALUATION ===\n"
    )

    for result in results:

        print(result)


if __name__ == "__main__":

    asyncio.run(main())
