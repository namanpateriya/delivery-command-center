class WorkflowPlanner:

    def create_plan(
        self,
        user_query: str
    ):

        plan = []

        query = user_query.lower()

        if (
            "project" in query
            or "status" in query
            or "delivery" in query
            or "timeline" in query
        ):
            plan.append(
                "delivery"
            )

        if (
            "risk" in query
            or "delay" in query
            or "blocked" in query
            or "issue" in query
        ):
            plan.append(
                "risk"
            )

        if (
            "leadership" in query
            or "stakeholder" in query
            or "communication" in query
            or "update" in query
        ):
            plan.append(
                "communication"
            )

        if not plan:

            plan = [
                "delivery",
                "risk",
                "communication"
            ]

        return plan
