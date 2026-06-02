class WorkflowPlanner:

    def create_plan(
        self,
        user_query: str
    ):

        plan = []

        query = user_query.lower()

        if any(
            keyword in query
            for keyword in [
                "project",
                "status",
                "delivery",
                "timeline"
            ]
        ):
            plan.append(
                "delivery"
            )

        if any(
            keyword in query
            for keyword in [
                "risk",
                "delay",
                "blocked",
                "issue"
            ]
        ):
            plan.append(
                "risk"
            )

        if any(
            keyword in query
            for keyword in [
                "leadership",
                "executive",
                "sponsor",
                "stakeholder",
                "communication",
                "update"
            ]
        ):
            plan.append(
                "communication"
            )

        if not plan:

            return [
                "delivery",
                "risk",
                "communication"
            ]

        return plan
