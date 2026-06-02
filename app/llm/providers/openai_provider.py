from openai import OpenAI

from app.config import (
    OPENAI_API_KEY,
    OPENAI_MODEL
)


class OpenAIProvider:

    def __init__(self):

        if not OPENAI_API_KEY:

            raise ValueError(
                "OPENAI_API_KEY not configured."
            )

        self.client = OpenAI(
            api_key=OPENAI_API_KEY
        )

    async def generate(
        self,
        prompt: str
    ):

        try:

            response = (
                self.client.responses.create(
                    model=OPENAI_MODEL,
                    input=prompt
                )
            )

            return {

                "provider": "openai",

                "content": getattr(
                    response,
                    "output_text",
                    ""
                )
            }

        except Exception as e:

            return {

                "provider": "openai",

                "error": str(e),

                "content": ""
            }
