from app.llm.provider_factory import (
    ProviderFactory
)

from app.llm.prompts import (
    DELIVERY_ANALYSIS_PROMPT,
    RISK_ANALYSIS_PROMPT,
    COMMUNICATION_PROMPT
)


class ReasoningEngine:

    def __init__(self):

        self.provider = (
            ProviderFactory
            .get_provider()
        )

    async def analyze_delivery(
        self,
        context
    ):

        prompt = (
            DELIVERY_ANALYSIS_PROMPT
            .format(
                context=context
            )
        )

        response = await self.provider.generate(
            prompt
        )
        
        return response.get(
            "content",
            ""
        )

    async def analyze_risk(
        self,
        context
    ):

        prompt = (
            RISK_ANALYSIS_PROMPT
            .format(
                context=context
            )
        )

        response = await self.provider.generate(
            prompt
        )
        
        return response.get(
            "content",
            ""
        )

    async def generate_communication(
        self,
        context
    ):

        prompt = (
            COMMUNICATION_PROMPT
            .format(
                context=context
            )
        )

        response = await self.provider.generate(
            prompt
        )
        
        return response.get(
            "content",
            ""
        )
