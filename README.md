# GitHub Repository Health Analyzer

## Part 1 — Project Description

### Overview

**GitHub Repository Health Analyzer** is a web-based application designed to evaluate the overall health and quality of a GitHub repository.

The user provides a GitHub repository URL, for example:

```text
https://github.com/username/repository
```

The application collects repository information through the GitHub API, analyzes repository structure and project files, calculates health metrics, and presents the results through a React dashboard.

### Main Goal

The main goal of the project is to help developers quickly understand the documentation, testing, code organization, security indicators, and maintainability of a GitHub repository.

### Health Metrics

The analyzer evaluates five major areas:

* **Documentation**
* **Testing**
* **Code Structure**
* **Security**
* **Maintainability**

Each category contributes up to **20 points**, producing an overall Repository Health Score out of **100**.

### Technology Stack

#### Frontend

* React
* Vite
* JavaScript
* CSS
* Recharts *(planned)*

#### Backend

* Python
* FastAPI
* Uvicorn
* HTTPX
* Pydantic

#### External API

* GitHub REST API

#### Planned Analysis Tools

* Radon for Python code complexity
* Bandit for Python security analysis
* Dependency analysis
* GitHub repository and commit data

#### Planned Database

* PostgreSQL

### Basic Architecture

```text
User
  |
  v
React Frontend
  |
  | Repository URL
  v
FastAPI Backend
  |
  +------> GitHub REST API
  |
  +------> Repository / Code Analysis
  |
  v
Analysis Modules
  |
  v
Score Calculation Engine
  |
  v
JSON Analysis Result
  |
  v
React Dashboard
```

---

# Part 2 — Project Roadmap

## Phase 1 — React Project Setup

**Goal:** Create the frontend foundation.

### Tasks

* Create React project using Vite
* Install dependencies
* Configure the main React files
* Understand Vite project structure
* Create the basic application structure

**Status:** ✅ Completed

---

## Phase 2 — Frontend UI

**Goal:** Build the basic user interface.

### Implemented

* Navbar
* Home page
* Project title and description
* Repository URL input
* Analyze Repository button
* Basic layout and styling

**Status:** ✅ Completed

---

## Phase 3 — Frontend Interactivity

**Goal:** Make the React interface functional.

### Implemented

* React `useState`
* Repository URL handling
* Button click handling
* Input validation
* Loading state
* Error handling
* Backend API request flow
* Backend result handling

**Status:** ✅ Completed

---

## Phase 4 — FastAPI Backend

**Goal:** Create the backend API.

### Implemented

* Python backend
* Virtual environment
* FastAPI
* Uvicorn
* HTTPX
* Pydantic
* `main.py`
* `GET /`
* `POST /analyze`
* GitHub URL validation
* Pydantic request model
* GitHub API connection structure

**Status:** ✅ Completed

### API Documentation

Swagger documentation is available at:

```text
http://127.0.0.1:8000/docs
```

---

## Phase 5 — GitHub API Integration

**Goal:** Collect repository information from GitHub.

### Implemented

* GitHub URL validation
* GitHub username extraction
* Repository name extraction
* GitHub API request structure
* Request headers
* HTTP timeout handling
* HTTP status handling
* Invalid response handling
* Repository information retrieval
* Repository file retrieval

**Status:** ✅ Completed

---

## Phase 6 — Repository Analysis Engine

**Goal:** Analyze the contents and structure of a GitHub repository.

### Analysis Areas

* Repository information
* Repository file structure
* Documentation
* Testing
* Code Structure
* Security
* Maintainability

The analyzer processes repository information and file paths returned by the GitHub API.

**Status:** 🟡 Implemented and being improved

---

## Phase 7 — Documentation Analysis

**Goal:** Evaluate repository documentation.

### Current Checks

* README availability
* Repository description
* Primary programming language
* Documentation-related information

The analyzer generates a documentation score and supporting details.

**Status:** ✅ Implemented

---

## Phase 8 — Testing Analysis

**Goal:** Detect testing-related files and evaluate repository testing support.

### Current Checks

* Test directories
* Test files
* `.test.js`, `.test.jsx`, `.test.ts`, `.test.tsx`
* `.spec.js`, `.spec.jsx`, `.spec.ts`, `.spec.tsx`
* Python test files
* Testing framework configuration
* Testing dependency indicators
* Multiple test files
* Test-related scripts/configuration

The analyzer generates a testing score out of 20 and descriptive analysis details.

**Status:** ✅ Implemented / Being improved

---

## Phase 9 — Code Structure Analysis

**Goal:** Evaluate how well the repository is organized.

### Current Checks

* Common project folders
* Source file count
* Configuration files
* Repository subdirectories
* Overall file organization

### Detected Project Folders

```text
src/
app/
components/
backend/
frontend/
api/
utils/
services/
models/
controllers/
```

### Detected Configuration Files

```text
package.json
requirements.txt
pyproject.toml
pom.xml
build.gradle
vite.config.js
vite.config.ts
tsconfig.json
```

The analyzer returns both a numerical score and human-readable analysis messages.

**Status:** ✅ Implemented and tested

---

## Phase 9.1 — Score Dashboard

**Goal:** Display repository health scores through a clear dashboard.

### Implemented

* Overall Repository Health card
* Overall health score
* `/100` score display
* Overall progress bar
* Documentation score
* Testing score
* Code Structure score
* Security score
* Maintainability score
* Category progress bars
* Responsive score layout

**Status:** ✅ Completed

---

## Phase 9.2 — Dashboard CSS Styling

**Goal:** Improve the visual appearance of the score dashboard.

### Implemented

* Dashboard cards
* Rounded cards
* Shadows
* Progress bars
* Category score cards
* Responsive layout
* Mobile-friendly layout
* Improved spacing and typography

**Status:** ✅ Completed

---

## Phase 9.3 — Repository Information Section

**Goal:** Display repository information in a structured dashboard section.

### Implemented

* Repository name
* Programming language
* Stars
* Forks
* Open issues
* Default branch
* Repository description
* GitHub repository link
* Responsive repository information card

**Status:** ✅ Implemented / Testing

---

## Phase 9.4 — Detailed Analysis Cards

**Goal:** Display detailed analysis findings for each health category.

### Planned Structure

```text
Analysis Details
       |
       +---- Documentation
       |       +---- Success
       |       +---- Warning
       |
       +---- Testing
       |       +---- Success
       |       +---- Warning
       |
       +---- Code Structure
       |       +---- Success
       |       +---- Warning
       |
       +---- Security
       |       +---- Success
       |       +---- Warning
       |
       +---- Maintainability
               +---- Success
               +---- Warning
```

**Status:** 🔄 In Progress

---

# Phase 10 — Security Analysis

**Goal:** Detect repository security indicators and potentially sensitive files.

### Current Checks

* `.gitignore`
* Environment template files
* Security documentation
* Dependency/configuration files
* Potentially sensitive filenames
* `.env` files
* Credential files
* Secret files
* `.pem` files
* `.key` files
* SSH private key indicators

### Security Scoring

The current security score has a maximum of **20 points**.

```text
.gitignore                         +4
Environment template              +3
Security documentation            +3
Dependency/configuration files    +3
No obvious sensitive files        +7
                                   ---
Maximum                           20
```

### Important Limitation

The current analyzer examines **repository file paths**.

It does **not yet claim to scan source-file contents or detect actual exposed secrets**.

Advanced security analysis using tools such as Bandit and dependency vulnerability scanning is planned for a future phase.

**Status:** ✅ Basic analysis implemented

---

# Phase 11 — Maintainability Analysis

**Goal:** Evaluate repository organization and maintainability indicators.

### Current Checks

* README/documentation
* Organized project folders
* Source-file count
* Dependency/configuration management
* Temporary or backup-looking files

### Maintainability Scoring

The current maintainability score has a maximum of **20 points**.

```text
README/documentation             +4
Organized source structure       +4
Source-file organization         +4
Configuration/dependencies       +4
No temporary/backup files        +4
                                  ---
Maximum                          20
```

### Important Limitation

The current implementation analyzes repository **file paths and structure**.

It does not yet perform advanced code-complexity or duplicate-code analysis.

Future versions may integrate tools such as Radon for Python complexity analysis.

**Status:** ✅ Basic analysis implemented

---

# Phase 12 — Health Scoring Engine

**Goal:** Combine the five analysis categories into an overall health score.

### Scoring Structure

```text
Documentation       /20
Testing             /20
Code Structure      /20
Security            /20
Maintainability     /20
                    ----
Overall             /100
```

The analyzer calculates the overall score by combining the five category scores.

```text
Overall Score =
Documentation
+ Testing
+ Code Structure
+ Security
+ Maintainability
```

**Status:** 🔄 Implemented and being refined

---

# Phase 13 — Recommendations

**Goal:** Provide useful suggestions based on detected repository issues.

### Planned Recommendations

* Improve README documentation
* Add testing support
* Improve project organization
* Add missing configuration files
* Improve dependency management
* Reduce code complexity
* Address security issues
* Improve maintainability

**Status:** ⏳ Pending

---

# Phase 14 — React + FastAPI Integration

**Goal:** Connect the backend analysis system with the React frontend.

### Implemented

* Repository URL input
* React state management
* Analysis request flow
* Loading state
* Error handling
* Backend API request
* Repository information display
* Health score display
* Category score display

### Remaining Improvements

* Display all backend analysis details
* Improve detailed analysis cards
* Refine API response handling
* Improve frontend error states
* Improve presentation of analysis results

**Status:** 🔄 In Progress

---

# Phase 15 — Dashboard and Visualization

**Goal:** Present repository analysis clearly through a complete dashboard.

### Implemented

* Overall health score
* Documentation score
* Testing score
* Code Structure score
* Security score
* Maintainability score
* Progress bars
* Repository statistics
* Repository information
* Responsive dashboard layout

### Planned

* Detailed analysis cards
* Charts
* Detected issues
* Recommendations
* Advanced visualizations

**Status:** 🔄 In Progress

---

# Phase 16 — Final Backend Testing

**Goal:** Verify that all five analysis modules work together correctly.

### Tested Flow

```text
GitHub Repository URL
          |
          v
     POST /analyze
          |
          v
    Validate URL
          |
          v
    GitHub REST API
          |
          v
 Repository Information
          |
          v
   Repository Files
          |
          v
   Analysis Modules
          |
          +---- Documentation
          |
          +---- Testing
          |
          +---- Code Structure
          |
          +---- Security
          |
          +---- Maintainability
          |
          v
    Health Score /100
          |
          v
       JSON Result
```

### Backend Verification

The backend can be tested through:

```text
http://127.0.0.1:8000/docs
```

The `POST /analyze` endpoint is used to submit a GitHub repository URL and receive the analysis response.

### Five-Category Result

The expected analysis structure is:

```json
{
  "health_score": {
    "overall": 70,
    "documentation": {
      "score": 15,
      "details": []
    },
    "testing": {
      "score": 8,
      "details": []
    },
    "code_structure": {
      "score": 17,
      "details": []
    },
    "security": {
      "score": 14,
      "details": []
    },
    "maintainability": {
      "score": 16,
      "details": []
    }
  }
}
```

The actual scores depend on the repository being analyzed.

**Status:** ✅ Completed / Verified

---

# Phase 17 — Scoring Accuracy Improvement

**Goal:** Improve the accuracy and reliability of repository health scoring.

### Planned Improvements

* Improve test detection
* Improve configuration detection
* Reduce false positives
* Improve security file detection
* Improve maintainability rules
* Improve source-file classification
* Refine category scoring weights
* Test against multiple repository types
* Compare analysis results across different GitHub repositories

**Status:** 🚀 Next Phase

---

# Phase 18 — Advanced Security and Code Analysis

**Goal:** Introduce deeper analysis beyond repository file paths.

### Planned Features

* Bandit security analysis
* Dependency vulnerability analysis
* Python code complexity analysis
* Radon integration
* Secret detection
* Dependency version analysis
* Code-quality checks
* Advanced security indicators

**Status:** ⏳ Future Phase

---

# Phase 19 — Recommendations Engine

**Goal:** Generate actionable recommendations from analysis results.

### Planned Features

* Category-specific recommendations
* Documentation suggestions
* Testing suggestions
* Security suggestions
* Maintainability suggestions
* Code organization suggestions
* Priority-based recommendations

**Status:** ⏳ Future Phase

---

# Phase 20 — Database and Analysis History

**Goal:** Store previous repository analyses.

### Planned Features

* PostgreSQL database
* Analysis history
* Repository history
* Score changes over time
* Previous reports
* Repository comparison
* Historical score charts

**Status:** ⏳ Future Phase

---

# Phase 21 — Advanced Features

### Possible Future Features

* AI-generated recommendations
* Dependency health analysis
* Git activity analysis
* Repository comparison
* PDF reports
* Score history charts
* Authentication
* Saved repositories
* Deployment

**Status:** ⏳ Future Scope

---

# Part 3 — Current Progress

## Current Project Structure

```text
github-health-analyzer/
│
├── .gitignore
│
├── backend/
│   ├── main.py
│   ├── github_api.py
│   ├── health_analyzer.py
│   ├── requirements.txt
│   └── venv/
│
├── src/
│   ├── components/
│   │   ├── Home.jsx
│   │   └── Navbar.jsx
│   ├── App.jsx
│   ├── App.css
│   ├── index.css
│   └── main.jsx
│
├── public/
├── package.json
├── package-lock.json
└── vite.config.js
```

---

# Frontend Progress

The React/Vite frontend has been successfully created and developed incrementally.

### Implemented

* React + Vite setup
* `App.jsx`
* `Navbar.jsx`
* `Home.jsx`
* Basic application structure
* Repository URL input
* React state using `useState`
* Analyze Repository button
* Loading state
* Error handling
* Repository analysis request
* Overall health score dashboard
* Category score cards
* Category progress bars
* Responsive dashboard styling
* Repository information section
* Repository statistics
* Repository description
* GitHub repository link

### Current Frontend Flow

```text
User enters GitHub URL
        |
        v
React stores URL in state
        |
        v
Analyze Repository button
        |
        v
FastAPI API request
        |
        v
Backend analyzes repository
        |
        v
JSON analysis response
        |
        v
React Dashboard
        |
        +---- Overall Health Score
        |
        +---- Category Scores
        |
        +---- Repository Information
        |
        +---- Analysis Details
```

---

# Backend Progress

The FastAPI backend has been successfully created and the main analysis pipeline is functional.

### Implemented

* Python virtual environment
* FastAPI
* Uvicorn
* HTTPX
* Pydantic
* `main.py`
* `github_api.py`
* `health_analyzer.py`
* `requirements.txt`
* `GET /`
* `POST /analyze`
* GitHub URL validation
* GitHub username/repository extraction
* GitHub API request structure
* Repository information retrieval
* Repository file retrieval
* Documentation scoring
* Testing scoring
* Code Structure scoring
* Code Structure analysis details
* Security scoring
* Security analysis details
* Maintainability scoring
* Maintainability analysis details
* Overall health score calculation

---

# Current Backend Flow

```text
POST /analyze
      |
      v
Receive repository URL
      |
      v
Validate GitHub URL
      |
      v
Extract username + repository
      |
      v
Call GitHub API
      |
      v
Get repository information
      |
      v
Get repository files
      |
      v
Run analysis modules
      |
      +----> Documentation
      |
      +----> Testing
      |
      +----> Code Structure
      |
      +----> Security
      |
      +----> Maintainability
      |
      v
Calculate scores
      |
      v
Return JSON response
```

---

# Current Analysis Categories

## Documentation

Checks documentation-related repository indicators such as:

* README
* Repository description
* Programming language
* Documentation information

**Maximum Score:** 20

---

## Testing

Checks:

* Test directories
* Test files
* Testing frameworks
* Testing dependencies
* Multiple test files
* Test-related configuration

**Maximum Score:** 20

---

## Code Structure

Checks:

* Project folders
* Source files
* Configuration files
* Repository organization
* Directory structure

**Maximum Score:** 20

---

## Security

Checks:

* `.gitignore`
* Environment templates
* Security documentation
* Dependency/configuration files
* Potentially sensitive filenames
* Key and certificate file indicators

**Maximum Score:** 20

**Current limitation:** Security analysis currently works primarily from repository file paths and does not yet scan file contents for actual secrets.

---

## Maintainability

Checks:

* README/documentation
* Organized project folders
* Source-file count
* Configuration/dependency files
* Temporary or backup-looking files

**Maximum Score:** 20

**Current limitation:** Advanced code complexity and duplicate-code analysis are not yet implemented.

---

# API Response Structure

The `/analyze` endpoint is designed around the following structure:

```json
{
  "message": "Repository analyzed successfully",
  "repository": {
    "name": "Github-Health-Analyze"
  },
  "health_score": {
    "overall": 70,
    "documentation": {
      "score": 15,
      "details": []
    },
    "testing": {
      "score": 8,
      "details": []
    },
    "code_structure": {
      "score": 17,
      "details": []
    },
    "security": {
      "score": 14,
      "details": []
    },
    "maintainability": {
      "score": 16,
      "details": []
    }
  }
}
```

The exact scores depend on the repository being analyzed.

---

# Current Development Status

## Completed

* ✅ React/Vite project setup
* ✅ Basic frontend UI
* ✅ Repository URL input
* ✅ React state management
* ✅ FastAPI backend
* ✅ GitHub URL validation
* ✅ GitHub API integration
* ✅ Repository information retrieval
* ✅ Repository file retrieval
* ✅ Documentation analysis
* ✅ Testing analysis foundation
* ✅ Code Structure scoring
* ✅ Code Structure detail analysis
* ✅ Security analysis
* ✅ Maintainability analysis
* ✅ Overall health score
* ✅ Category score cards
* ✅ Progress bars
* ✅ Dashboard CSS styling
* ✅ Responsive dashboard layout
* ✅ Repository information section
* ✅ Final backend analysis flow testing

## Currently Working On

* 🔄 Improving scoring accuracy
* 🔄 Testing the analyzer with different GitHub repositories
* 🔄 Improving React + FastAPI integration
* 🔄 Displaying all backend analysis details in the frontend
* 🔄 Improving detailed analysis cards
* 🔄 Improving repository statistics presentation

## Next Development Step

### Phase 17 — Improving Scoring Accuracy

The next development phase will focus on making the analyzer more reliable across different types of GitHub repositories.

The planned work includes:

```text
Repository Testing
       |
       v
Identify False Positives
       |
       v
Improve Detection Rules
       |
       v
Refine Scoring Weights
       |
       v
Test Multiple Repositories
       |
       v
Improve Health Score Accuracy
```

---

# Project Development Principle

The project is being developed incrementally.

Each feature is implemented, tested, and verified before moving to the next stage.

The target final workflow is:

```text
GitHub Repository URL
          |
          v
      React UI
          |
          v
     FastAPI Backend
          |
          v
     GitHub REST API
          |
          v
 Repository Data + Files
          |
          v
    Analysis Modules
          |
          v
     Scoring Engine
          |
          v
 Health Score + Metrics
          |
          v
 Recommendations
          |
          v
 React Dashboard
          |
          v
 Reports / History
```

## Current Milestone

**The GitHub Repository Health Analyzer now has a functional FastAPI backend with five analysis categories — Documentation, Testing, Code Structure, Security, and Maintainability — along with an initial React dashboard for displaying repository health scores and repository information.**

The latest completed work includes:

* **Security Analysis**
* **Maintainability Analysis**
* **Five-category health scoring**
* **Final backend testing**
* **Initial React dashboard**
* **Repository information display**
* **Responsive score dashboard**

The **next development step is Phase 17 — Improving Scoring Accuracy**, followed by deeper analysis, detailed recommendations, advanced visualization, database/history, and deployment.
