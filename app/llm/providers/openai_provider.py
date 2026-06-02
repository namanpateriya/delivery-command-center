from openai import OpenAI

from app.config import (
    OPENAI_API_KEY,
    OPENAI_MODEL
)


class OpenAIProvider:

    def __init__(self):

        self.client = OpenAI(
            api_key=OPENAI_API_KEY
        )

    async def generate(
        self,
        prompt: str
    ):

        response = (
            self.client.responses.create(
                model=OPENAI_MODEL,
                input=prompt
            )
        )

        return response.output_text
