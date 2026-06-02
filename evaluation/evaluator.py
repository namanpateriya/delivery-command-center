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

        result = await service.execute(
            (
                "Project delayed by "
                "3 weeks."
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
                "executive_summary",

                "passed":
                (
                    "executive_summary"
                    in result
                )
            },

            {
                "test":
                "readiness_score",

                "passed":
                (
                    optimization[
                        "readiness_score"
                    ] >= 60
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
                    != "High Risk"
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

    print(results)


if __name__ == "__main__":

    asyncio.run(main())
