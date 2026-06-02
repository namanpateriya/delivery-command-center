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

        report = (
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

        metrics = (
            optimizer.optimize(
                report
            )
        )

        tests = [

            {
                "test":
                "executive_summary",

                "passed":
                bool(
                    report.get(
                        "executive_summary"
                    )
                )
            },

            {
                "test":
                "delivery_analysis",

                "passed":
                bool(
                    report.get(
                        "delivery_analysis"
                    )
                )
            },

            {
                "test":
                "risk_analysis",

                "passed":
                bool(
                    report.get(
                        "risk_analysis"
                    )
                )
            },

            {
                "test":
                "stakeholder_update",

                "passed":
                bool(
                    report.get(
                        "stakeholder_update"
                    )
                )
            },

            {
                "test":
                "governance_score",

                "passed":
                (
                    metrics[
                        "governance_score"
                    ] >= 80
                )
            }
        ]

        passed = len(
            [
                t
                for t in tests
                if t["passed"]
            ]
        )

        total = len(
            tests
        )

        return {

            "score":
            round(
                (
                    passed / total
                ) * 100,
                2
            ),

            "tests":
            tests,

            "metrics":
            metrics
        }


async def main():

    evaluator = (
        WorkflowEvaluator()
    )

    result = (
        await evaluator.evaluate()
    )

    print(
        "\n=== EVALUATION ===\n"
    )

    print(result)


if __name__ == "__main__":

    asyncio.run(main())
