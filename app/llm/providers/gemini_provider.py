from google import genai

from app.config import (
    GEMINI_API_KEY,
    GEMINI_MODEL
)


class GeminiProvider:

    def __init__(self):

        if not GEMINI_API_KEY:

            raise ValueError(
                "GEMINI_API_KEY not configured."
            )

        self.client = genai.Client(
            api_key=GEMINI_API_KEY
        )

    async def generate(
        self,
        prompt: str
    ):

        try:

            response = (
                self.client.models.generate_content(
                    model=GEMINI_MODEL,
                    contents=prompt
                )
            )

            return {

                "provider": "gemini",

                "content": getattr(
                    response,
                    "text",
                    ""
                )
            }

        except Exception as e:

            return {

                "provider": "gemini",

                "error": str(e),

                "content": ""
            }
