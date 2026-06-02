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
                    "executive leadership "
                    "update."
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
                    ] >= 50
                )
            },

            {
                "test":
                "agent_participation",

                "passed":
                (
                    metrics[
                        "agent_participation_score"
                    ] >= 50
                )
            }
        ]

        passed = len(
            [
                test
                for test in tests
                if test["passed"]
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
            metrics,

            "report":
            report
        }


async def main():

    evaluator = (
        WorkflowEvaluator()
    )

    results = (
        await evaluator.evaluate()
    )

    print(
        "\n=== DELIVERY COMMAND CENTER EVALUATION ===\n"
    )

    print(results)


if __name__ == "__main__":

    asyncio.run(main())
