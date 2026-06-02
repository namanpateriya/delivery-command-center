from app.mcp.resources import (
    PROJECT_STATUS,
    PROJECT_RISKS,
    STAKEHOLDERS
)


def generate_project_summary():

    return {
        "summary": PROJECT_STATUS["summary"],
        "health": PROJECT_STATUS["health"]
    }


def assess_project_risk():

    high_risks = [
        risk
        for risk in PROJECT_RISKS
        if risk["severity"] == "High"
    ]

    return {
        "high_risk_count": len(high_risks),
        "overall_risk": (
            "High"
            if high_risks
            else "Medium"
        )
    }


def draft_status_update():

    return {
        "message": (
            "Project delivery is currently Amber. "
            "Primary delays are associated with "
            "vendor dependencies. Mitigation plans "
            "have been initiated."
        )
    }
