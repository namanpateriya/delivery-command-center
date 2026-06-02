class ResultAggregator:

    def aggregate(
        self,
        plan,
        results
    ):

        output = {

            "summary": "",

            "risks": [],

            "recommended_actions": [],

            "communication_draft": ""
        }

        for task, result in zip(
            plan,
            results
        ):

            if task == "delivery":

                output[
                    "summary"
                ] = result

            elif task == "risk":

                output[
                    "risks"
                ].append(
                    result
                )

                output[
                    "recommended_actions"
                ].append(
                    (
                        "Review open "
                        "project risks."
                    )
                )

            elif task == (
                "communication"
            ):

                output[
                    "communication_draft"
                ] = result

        return {

            "executive_summary":
            output
        }
