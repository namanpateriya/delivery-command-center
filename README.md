# Delivery Command Center

Delivery Command Center is an MCP-powered AI system designed for Program Managers, Delivery Leaders, PMOs, and Customer Success teams.

The repository demonstrates how multiple AI agents can collaborate to analyze delivery health, identify risks, generate executive communications, and provide governance-focused recommendations.

Unlike traditional assistants, this project combines:

- Multi-Agent Architecture
- MCP (Model Context Protocol)
- Multi-LLM Support
- Workflow Orchestration
- Executive Reporting
- Evaluation & Optimization

---

# Why This Repository?

Program Managers spend significant effort collecting information from multiple sources before preparing:

- Executive Status Reports
- Risk Reviews
- Leadership Updates
- Governance Reviews
- Stakeholder Communications

This repository demonstrates how MCP and AI agents can work together to automate portions of that workflow.

---

# Key Features

## MCP Integration

Uses MCP resources and tools to access project information.

## Multi-Agent Collaboration

Specialized agents independently analyze:

- Delivery Health
- Project Risks
- Stakeholder Communication

## Multi-LLM Support

Provider abstraction supports:

- Gemini
- OpenAI
- Anthropic (Stub)
- AWS Bedrock (Stub)

Provider selection is controlled through environment variables.

## Workflow Orchestration

Planner, Router, and Aggregator coordinate execution across agents.

## Executive Reporting

Produces structured leadership-ready outputs.

## Evaluation & Optimization

Built-in evaluation framework assesses:

- Governance readiness
- Workflow completeness
- Agent participation
- Communication coverage

## MCP Fallback Mode

Application can operate without MCP by loading data directly from JSON files.

---

# Architecture Overview

User Query
      ↓

Workflow Planner
      ↓

Agent Router
      ↓

┌─────────────────┐
│ Delivery Agent  │
└─────────────────┘

┌─────────────────┐
│ Risk Agent      │
└─────────────────┘

┌─────────────────┐
│ Communication   │
│ Agent           │
└─────────────────┘

      ↓

Reasoning Engine
      ↓

Provider Factory
      ↓

Gemini / OpenAI

      ↓

MCP Client
      ↓

MCP Server

OR

JSON Fallback

      ↓

Aggregator
      ↓

Executive Report
      ↓

Optimizer
      ↓

Evaluator

---

# Supported Providers

## Gemini

```env
LLM_PROVIDER=gemini
```

## OpenAI

```env
LLM_PROVIDER=openai
```

## Anthropic

```env
LLM_PROVIDER=anthropic
```

(Currently Stub)

## AWS Bedrock

```env
LLM_PROVIDER=bedrock
```

(Currently Stub)

---

# Running the Application

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

## API

```bash
uvicorn app.main:app --reload
```

Open:

```text
http://localhost:8000/docs
```

---

## CLI

```bash
python -m app.cli \
--query "Project delayed by 3 weeks. Prepare leadership update."
```

---

# MCP Mode

```env
ENABLE_MCP=true
```

Uses:

- MCP Resources
- MCP Tools
- MCP Discovery

---

# Fallback Mode

```env
ENABLE_MCP=false
```

Uses:

- sample_project.json
- sample_risks.json
- sample_stakeholders.json

No MCP server required.

---

# Evaluation

Run:

```bash
python -m evaluation.evaluator
```

The framework evaluates:

- Delivery Analysis
- Risk Analysis
- Stakeholder Communication
- Governance Readiness
- Agent Participation

---

# Enterprise Applications

Potential use cases include:

- Program Management
- PMO Operations
- Customer Success
- Transformation Offices
- Delivery Governance
- Executive Reporting

---

# Learning Outcomes

This repository demonstrates:

- MCP Integration
- Multi-Agent Systems
- Multi-LLM Architecture
- Provider Abstraction
- Workflow Orchestration
- Governance-focused Evaluation

---

# Future Enhancements

Potential extensions include:

- Jira Integration
- Confluence Integration
- RAG Support
- Long-Term Memory
- Multi-MCP Server Support
- Anthropic Support
- AWS Bedrock Support

---

# Summary

Delivery Command Center demonstrates how MCP, AI agents, workflow orchestration, and modern LLM architectures can be combined to build enterprise-grade delivery intelligence systems.
