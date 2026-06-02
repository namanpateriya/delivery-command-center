from typing import List
from pydantic import BaseModel


class ProjectStatus(BaseModel):

    project_name: str
    health: str
    timeline_status: str
    summary: str


class Risk(BaseModel):

    risk_id: str
    description: str
    severity: str


class Stakeholder(BaseModel):

    name: str
    role: str
    email: str


class ExecutiveReport(BaseModel):

    summary: str

    risks: List[str]

    actions: List[str]

    communication_draft: str


class AgentResponse(BaseModel):

    agent_name: str

    output: dict


class WorkflowResponse(BaseModel):

    status: str

    report: ExecutiveReport
