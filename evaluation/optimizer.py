class WorkflowOptimizer:

    def optimize(
        self,
        report: dict
    ):

        delivery_score = 0
        risk_score = 0
        communication_score = 0

        recommendations = []

        if report.get(
            "delivery_analysis"
        ):

            delivery_score = 100

        else:

            recommendations.append(
                (
                    "Delivery analysis "
                    "needs improvement."
                )
            )

        if report.get(
            "risk_analysis"
        ):

            risk_score = 100

        else:

            recommendations.append(
                (
                    "Risk visibility "
                    "is insufficient."
                )
            )

        if report.get(
            "stakeholder_update"
        ):

            communication_score = 100

        else:

            recommendations.append(
                (
                    "Leadership update "
                    "is missing."
                )
            )

        governance_score = int(
            (
                delivery_score +
                risk_score +
                communication_score
            ) / 3
        )

        readiness_score = (
            governance_score
        )

        agent_participation_score = (
            len(
                [
                    x
                    for x in [
                        delivery_score,
                        risk_score,
                        communication_score
                    ]
                    if x > 0
                ]
            )
            / 3
        ) * 100

        return {

            "delivery_score":
            delivery_score,

            "risk_score":
            risk_score,

            "communication_score":
            communication_score,

            "governance_score":
            governance_score,

            "readiness_score":
            readiness_score,

            "agent_participation_score":
            int(
                agent_participation_score
            ),

            "recommendations":
            recommendations
        }
