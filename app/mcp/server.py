import json

from mcp.server.fastmcp import FastMCP

from app.config import APP_NAME

from app.mcp.resources import (
    PROJECT_STATUS,
    PROJECT_MILESTONES,
    PROJECT_RISKS,
    STAKEHOLDERS
)

from app.mcp.tools import (
    generate_project_summary,
    assess_project_risk,
    draft_status_update
)

mcp = FastMCP(APP_NAME)


# ======================================
# PROJECT RESOURCES
# ======================================

@mcp.resource("project://status")
def project_status():

    return json.dumps(
        PROJECT_STATUS,
        indent=2
    )


@mcp.resource("project://milestones")
def project_milestones():

    return json.dumps(
        PROJECT_MILESTONES,
        indent=2
    )


# ======================================
# RISK RESOURCES
# ======================================

@mcp.resource("risk://open")
def open_risks():

    return json.dumps(
        PROJECT_RISKS,
        indent=2
    )


# ======================================
# STAKEHOLDER RESOURCES
# ======================================

@mcp.resource("stakeholder://contacts")
def stakeholder_contacts():

    return json.dumps(
        STAKEHOLDERS,
        indent=2
    )


# ======================================
# TOOLS
# ======================================

@mcp.tool(name="generate_project_summary")
def generate_project_summary_tool():

    return generate_project_summary()


@mcp.tool(name="assess_project_risk")
def assess_project_risk_tool():

    return assess_project_risk()


@mcp.tool(name="draft_status_update")
def draft_status_update_tool():

    return draft_status_update()


@mcp.tool(name="server_health")
def server_health():

    return {
        "status": "healthy"
    }


if __name__ == "__main__":

    mcp.run()
