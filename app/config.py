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
        "5"
    )
)

# ==========================
# LLM Configuration
# ==========================

LLM_PROVIDER = os.getenv(
    "LLM_PROVIDER",
    "gemini"
).lower()

# Gemini

GEMINI_API_KEY = os.getenv(
    "GEMINI_API_KEY",
    ""
)

GEMINI_MODEL = os.getenv(
    "GEMINI_MODEL",
    "gemini-2.5-flash"
)

# OpenAI

OPENAI_API_KEY = os.getenv(
    "OPENAI_API_KEY",
    ""
)

OPENAI_MODEL = os.getenv(
    "OPENAI_MODEL",
    "gpt-5"
)

# Anthropic

ANTHROPIC_API_KEY = os.getenv(
    "ANTHROPIC_API_KEY",
    ""
)

ANTHROPIC_MODEL = os.getenv(
    "ANTHROPIC_MODEL",
    "claude-sonnet-4"
)

# AWS Bedrock

AWS_REGION = os.getenv(
    "AWS_REGION",
    "us-east-1"
)

AWS_ACCESS_KEY_ID = os.getenv(
    "AWS_ACCESS_KEY_ID",
    ""
)

AWS_SECRET_ACCESS_KEY = os.getenv(
    "AWS_SECRET_ACCESS_KEY",
    ""
)

BEDROCK_MODEL = os.getenv(
    "BEDROCK_MODEL",
    "anthropic.claude-3-sonnet"
)

# ==========================
# Data Files
# ==========================

PROJECT_DATA_FILE = os.getenv(
    "PROJECT_DATA_FILE",
    "examples/sample_project.json"
)

RISK_DATA_FILE = os.getenv(
    "RISK_DATA_FILE",
    "examples/sample_risks.json"
)

STAKEHOLDER_DATA_FILE = os.getenv(
    "STAKEHOLDER_DATA_FILE",
    "examples/sample_stakeholders.json"
)
