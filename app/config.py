from dotenv import load_dotenv
import os

load_dotenv()


APP_NAME = os.getenv(
    "APP_NAME",
    "Delivery Command Center"
)

APP_VERSION = os.getenv(
    "APP_VERSION",
    "1.0.0"
)

LOG_LEVEL = os.getenv(
    "LOG_LEVEL",
    "INFO"
)

MAX_RISKS_IN_REPORT = int(
    os.getenv(
        "MAX_RISKS_IN_REPORT",
        5
    )
)
