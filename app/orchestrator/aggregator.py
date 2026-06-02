class ResultAggregator:

    def aggregate(
        self,
        delivery_result,
        risk_result,
        communication_result
    ):

        return {
            "executive_summary": {
                "delivery": delivery_result,
                "risk": risk_result,
                "communication": communication_result
            }
        }
