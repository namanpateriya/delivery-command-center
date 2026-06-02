import asyncio

from app.orchestrator.service import (
    DeliveryCommandCenter
)

from evaluation.optimizer import (
    WorkflowOptimizer
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
                    "3 weeks. Prepare "
                    "leadership update."
                )
            )
        )

        optimizer = (
            WorkflowOptimizer()
        )

        optimization = (
            optimizer.optimize(
                result
            )
        )

        tests = [

            {
                "test":
                "workflow_execution",

                "passed":
                result is not None
            },

            {
                "test":
                "coverage_score",

                "passed":
                (
                    optimization[
                        "coverage_score"
                    ] >= 75
                )
            },

            {
                "test":
                "governance_score",

                "passed":
                (
                    optimization[
                        "governance_score"
                    ] >= 75
                )
            },

            {
                "test":
                "readiness_score",

                "passed":
                (
                    optimization[
                        "readiness_score"
                    ] >= 75
                )
            },

            {
                "test":
                "governance_status",

                "passed":
                (
                    optimization[
                        "governance_status"
                    ]
                    == "Healthy"
                )
            }
        ]

        return {

            "tests": tests,

            "optimization":
            optimization
        }


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

    print(results)


if __name__ == "__main__":

    asyncio.run(main())
