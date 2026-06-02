from datetime import datetime, UTC


class ResultAggregator:

    def aggregate(
        self,
        query: str,
        plan: list[str],
        results: list[dict]
    ):

        report = {
            "generated_at": datetime.now(
                UTC
            ).isoformat(),
            "query": query,
            "executive_summary": "",
            "delivery_analysis": "",
            "risk_analysis": "",
            "stakeholder_update": "",
            "recommended_actions": []
        }

        for task, result in zip(
            plan,
            results
        ):

            if not result.get(
                "success",
                False
            ):
                continue

            if task == "delivery":

                report[
                    "delivery_analysis"
                ] = result.get(
                    "analysis",
                    ""
                )

            elif task == "risk":

                report[
                    "risk_analysis"
                ] = result.get(
                    "analysis",
                    ""
                )

                report[
                    "recommended_actions"
                ].append(
                    (
                        "Review critical risks "
                        "and mitigation plans."
                    )
                )

            elif task == "communication":

                report[
                    "stakeholder_update"
                ] = result.get(
                    "analysis",
                    ""
                )

        summary = []

        if report["delivery_analysis"]:
            summary.append(
                "Delivery assessment completed."
            )

        if report["risk_analysis"]:
            summary.append(
                "Risk review completed."
            )

        if report["stakeholder_update"]:
            summary.append(
                "Leadership communication prepared."
            )

        report[
            "executive_summary"
        ] = " ".join(summary)

        return report
