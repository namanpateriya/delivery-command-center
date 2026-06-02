# Architecture

## Purpose

Delivery Command Center demonstrates how MCP can be combined with AI agents and modern LLM providers to support enterprise delivery management workflows.

The architecture separates:

- Information Access
- Business Reasoning
- Workflow Execution
- Evaluation

into independent layers.

---

# Design Principles

## Separation of Concerns

Each layer has a dedicated responsibility.

## Provider Independence

Agents should not be coupled to a specific LLM.

## MCP First

Information should be accessible through MCP resources and tools.

## Reliability

Fallback mode ensures the system remains operational when MCP is unavailable.

---

# High-Level Architecture

User
 ↓
Planner
 ↓
Router
 ↓
Agents
 ↓
Reasoning Engine
 ↓
Provider Factory
 ↓
LLM Provider
 ↓
MCP / JSON
 ↓
Aggregator
 ↓
Optimizer
 ↓
Evaluator

---

# Agent Layer

## Delivery Agent

Responsible for:

- Project Health
- Timeline Assessment
- Delivery Recommendations

---

## Risk Agent

Responsible for:

- Risk Assessment
- Risk Prioritization
- Mitigation Recommendations

---

## Communication Agent

Responsible for:

- Leadership Updates
- Executive Summaries
- Stakeholder Communication

---

# Reasoning Layer

The Reasoning Engine converts structured project data into AI prompts.

Responsibilities:

- Prompt Construction
- Context Packaging
- Provider Invocation

---

# Provider Layer

Provider Factory dynamically selects the configured model.

Supported providers:

- Gemini
- OpenAI
- Anthropic (Stub)
- AWS Bedrock (Stub)

---

# MCP Layer

Provides standardized access to:

## Resources

```text
project://status
risk://open
stakeholder://contacts
```

## Tools

```text
generate_project_summary
assess_project_risk
draft_status_update
```

---

# Fallback Mode

If MCP is unavailable:

```env
ENABLE_MCP=false
```

data is loaded directly from JSON files.

Benefits:

- Simplified demos
- Improved reliability
- Reduced setup complexity

---

# Orchestration Layer

## Planner

Determines which tasks are required.

## Router

Maps tasks to agents.

## Aggregator

Combines outputs into a single executive report.

---

# Evaluation Layer

## Optimizer

Produces:

- Delivery Score
- Risk Score
- Communication Score
- Governance Score
- Readiness Score

## Evaluator

Validates workflow execution and report completeness.

---

# Extension Points

Potential future additions:

## Integrations

- Jira
- Confluence
- ServiceNow

## AI Capabilities

- RAG
- Memory
- Tool Calling
- Multi-MCP

## Providers

- Anthropic
- Bedrock
- Azure OpenAI

---

# Conclusion

The architecture demonstrates a practical enterprise pattern combining MCP, AI agents, workflow orchestration, and provider abstraction to support delivery management use cases.
