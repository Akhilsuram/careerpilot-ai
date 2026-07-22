# CareerPilot AI API Documentation

## Base URL

```
http://localhost:8000
```

---

# Resume APIs

## Upload Resume

**Endpoint**

```
POST /resume/upload
```

### Description

Uploads a PDF resume, extracts text, parses structured information, and stores it in the database.

### Request

- multipart/form-data
- PDF File

### Response

```json
{
  "message": "Resume uploaded successfully",
  "resume_id": 1
}
```

---

## Get Latest Resume

**Endpoint**

```
GET /resume/latest
```

### Description

Returns the latest uploaded resume.

---

# ATS APIs

## Analyze Resume

**Endpoint**

```
POST /ats/analyze
```

### Description

Analyzes the uploaded resume and generates an ATS score.

### Response

```json
{
    "score": 87,
    "missing_keywords": [],
    "suggestions": []
}
```

---

# Career Report APIs

## Generate AI Report

**Endpoint**

```
POST /report/generate
```

### Description

Generates a complete AI-powered career report.

Includes:

- Resume Summary
- Strengths
- Weaknesses
- Skill Gap
- Career Suggestions
- Learning Resources

---

# Resume Optimizer APIs

## Optimize Resume

**Endpoint**

```
POST /resume/optimize
```

### Description

Improves the uploaded resume using AI.

Returns:

- Optimized summary
- Improved experience
- Better wording
- ATS improvements

---

# Job Recommendation APIs

## Recommend Jobs

**Endpoint**

```
POST /jobs/recommend
```

### Description

Generates personalized job recommendations.

Returns:

- Job title
- Match percentage
- Required skills
- Recommendation reason

---

# Interview APIs

## Generate Interview Questions

**Endpoint**

```
POST /interview/questions
```

### Description

Creates personalized interview questions based on the uploaded resume.

Includes:

- HR Questions
- Technical Questions
- Resume Questions

---

# Career Roadmap APIs

## Generate Roadmap

**Endpoint**

```
POST /roadmap/generate
```

### Description

Creates a personalized learning roadmap.

Returns:

- Weekly goals
- Skills
- Resources
- Timeline

---

# Analytics APIs

## Dashboard Analytics

**Endpoint**

```
GET /analytics/dashboard
```

### Description

Returns dashboard statistics.

Includes:

- Total resumes
- ATS average
- Reports generated
- Jobs recommended

---

## ATS History

**Endpoint**

```
GET /analytics/ats-history
```

### Description

Returns ATS score history.

---

# History APIs

## Career History

**Endpoint**

```
GET /history
```

### Description

Returns previous analyses.

Includes:

- ATS Reports
- Career Reports
- Resume Optimizations
- Roadmaps
- Interview Sessions

---

# Response Codes

| Code | Meaning |
|------|---------|
| 200 | Success |
| 201 | Resource Created |
| 400 | Invalid Request |
| 404 | Resource Not Found |
| 422 | Validation Error |
| 500 | Internal Server Error |

---

# Authentication

Current Version

- No authentication

Future Version

- JWT Authentication
- User Accounts
- Role-Based Access