from app.agents.delivery_agent import (
    DeliveryAgent
)

from app.agents.risk_agent import (
    RiskAgent
)

from app.agents.communication_agent import (
    CommunicationAgent
)


class AgentRouter:

    def __init__(self):

        self.agent_map = {
            "delivery": DeliveryAgent(),
            "risk": RiskAgent(),
            "communication": CommunicationAgent()
        }

    def get_agent(
        self,
        task_name: str
    ):

        return self.agent_map[
            task_name
        ]
