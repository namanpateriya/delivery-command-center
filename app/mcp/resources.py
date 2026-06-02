from app.config import (
    PROJECT_DATA_FILE,
    RISK_DATA_FILE,
    STAKEHOLDER_DATA_FILE
)

from app.utils.json_loader import (
    load_json_file
)

PROJECT_STATUS = load_json_file(
    PROJECT_DATA_FILE
)

PROJECT_RISKS = load_json_file(
    RISK_DATA_FILE
)

STAKEHOLDERS = load_json_file(
    STAKEHOLDER_DATA_FILE
)

PROJECT_MILESTONES = {
    "requirements": "Completed",
    "development": "Completed",
    "testing": "In Progress",
    "production_release": "Delayed"
}
