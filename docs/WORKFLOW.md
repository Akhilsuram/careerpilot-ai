# CareerPilot AI Workflow

# Overview

CareerPilot AI follows a modular AI pipeline where each feature performs a specific task before passing the result to the next stage.

This architecture keeps the system modular, scalable, and easy to maintain.

---

# Complete Workflow

```
                    User
                      │
                      ▼
              Upload Resume (PDF)
                      │
                      ▼
              PDF Text Extraction
                      │
                      ▼
            Resume Parsing & Structuring
                      │
                      ▼
              Store Resume in Database
                      │
                      ▼
        Career Copilot Orchestrator
                      │
      ┌───────────────┼───────────────┐
      ▼               ▼               ▼
 ATS Analyzer   Career Report   Resume Optimizer
      │               │               │
      ├───────────────┼───────────────┤
      ▼               ▼               ▼
 Job Recommendation Interview Generator Roadmap Generator
      │               │               │
      └───────────────┼───────────────┘
                      ▼
            Store Results in Database
                      │
                      ▼
        Dashboard • Analytics • History
```

---

# Step 1 – Resume Upload

The user uploads a PDF resume from the frontend.

The backend validates:

- File type
- File size
- Upload integrity

---

# Step 2 – Resume Parsing

The PDF parser extracts text.

The Resume Agent converts the extracted text into structured data.

Example:

- Personal Information
- Skills
- Education
- Experience
- Projects
- Certifications

---

# Step 3 – Database Storage

The parsed resume is stored in SQLite for future processing.

---

# Step 4 – Career Copilot Orchestrator

The orchestrator coordinates all AI modules.

Instead of each module working independently, the orchestrator manages:

- Input
- AI Provider
- Prompt Flow
- Output
- Storage

---

# Step 5 – ATS Analysis

The ATS Analyzer evaluates the resume.

Outputs:

- ATS Score
- Missing Keywords
- Resume Suggestions
- Recruiter Feedback

---

# Step 6 – Career Report Generation

The Career Report Generator creates a personalized report.

Includes:

- Resume Summary
- Strengths
- Weaknesses
- Skill Gap
- Career Recommendations
- Learning Resources

---

# Step 7 – Resume Optimization

The Resume Optimizer improves:

- Summary
- Experience
- Bullet Points
- ATS Compatibility

---

# Step 8 – Job Recommendation

The Job Recommendation Agent recommends jobs based on:

- Skills
- Experience
- Resume Content
- Career Interests

---

# Step 9 – Interview Preparation

The Interview Agent generates:

- HR Questions
- Technical Questions
- Resume-Based Questions

---

# Step 10 – Career Roadmap

The Roadmap Agent creates a personalized learning plan.

Includes:

- Weekly Goals
- Learning Resources
- Skill Progression
- Estimated Timeline

---

# Step 11 – Database Update

Generated outputs are stored for future access.

Stored information includes:

- ATS Reports
- Career Reports
- Optimized Resumes
- Job Recommendations
- Interview Questions
- Roadmaps

---

# Step 12 – Dashboard

The dashboard summarizes:

- Resume Statistics
- ATS Performance
- Analytics
- Previous Activity

---

# AI Provider Flow

```
Career Copilot
        │
        ▼
Provider Manager
        │
        ▼
Provider Factory
        │
        ▼
Groq
or
OpenRouter
```

The Provider Manager selects the configured AI provider and forwards requests through a common interface.

---

# Error Handling

Every stage validates input before processing.

Examples:

- Invalid PDF
- Missing Resume
- AI Provider Failure
- Empty Response
- Database Error

Errors are returned as user-friendly messages instead of crashing the application.

---

# Summary

CareerPilot AI follows a multi-agent architecture coordinated by a central orchestrator.

Each agent has a dedicated responsibility, allowing the application to remain modular, scalable, and easy to extend with additional AI capabilities in future versions.