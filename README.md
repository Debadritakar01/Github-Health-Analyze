# GitHub Repository Health Analyzer

## Part 1 — Project Description

### Overview

**GitHub Repository Health Analyzer** is a web-based application designed to evaluate the overall health and quality of a GitHub repository.

The user provides a GitHub repository URL, for example:

```text
https://github.com/username/repository
```

The application collects repository information through the GitHub API, analyzes the repository structure and project files, calculates health metrics, and presents the results through a React dashboard.

### Main Goal

The main goal of the project is to help developers quickly understand the quality, maintainability, documentation, testing, structure, and security condition of a GitHub repository.

### Planned Health Metrics

The application evaluates the repository using areas such as:

* **Documentation**
* **Testing**
* **Code Structure**
* **Security**
* **Maintainability**

These individual metrics will contribute to an overall Repository Health Score out of 100.

### Technology Stack

**Frontend**

* React
* Vite
* JavaScript
* CSS
* Recharts *(planned)*

**Backend**

* Python
* FastAPI
* Uvicorn
* HTTPX
* Pydantic

**External API**

* GitHub REST API

**Planned Analysis Tools**

* Radon for Python code complexity
* Bandit for Python security analysis
* Dependency analysis
* GitHub repository and commit data

**Planned Database**

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
* Understand Vite project structure
* Configure the main React files
* Create the basic application structure

**Status:** ✅ Completed

---

## Phase 2 — Frontend UI

**Goal:** Build the basic user interface.

### Tasks

* Create Navbar
* Create Home page
* Add project title and description
* Add repository URL input
* Create Analyze Repository button
* Improve layout and styling

**Status:** ✅ Basic structure completed

---

## Phase 3 — Frontend Interactivity

**Goal:** Make the React interface functional.

### Tasks

* Use React `useState`
* Handle repository URL input
* Handle button click
* Validate user input
* Add loading state
* Add error messages
* Prepare API request
* Display backend results

**Status:** 🟡 Started

Repository URL state and input handling have been implemented. React-to-FastAPI integration is the next major frontend step.

---

## Phase 4 — FastAPI Backend

**Goal:** Create the backend API.

### Tasks

* Create Python backend folder
* Create virtual environment
* Install FastAPI, Uvicorn and HTTPX
* Create `main.py`
* Create GET `/` endpoint
* Create POST `/analyze` endpoint
* Validate repository URLs
* Add Pydantic request model
* Connect backend to GitHub API

**Status:** ✅ Mostly Completed

The FastAPI server is running successfully and the following endpoints are available:

```text
GET /
POST /analyze
```

Swagger documentation is available through:

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
* Invalid JSON response handling
* Repository information retrieval

**Status:** 🟡 In Progress

The backend can reach the GitHub API and repository analysis is being tested and improved.

---

## Phase 6 — Repository Analysis Engine

**Goal:** Analyze the contents of a GitHub repository.

### Implemented Analysis Areas

* Repository information
* Repository file structure
* Documentation
* Testing
* Code Structure
* Security
* Maintainability

The analyzer now processes repository file information returned by GitHub.

**Status:** 🟡 In Progress

The first detailed repository analysis modules have been implemented and are being tested incrementally.

---

## Phase 7 — Documentation Analysis

**Goal:** Evaluate the quality and availability of repository documentation.

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

### Planned Checks

* Test directories
* Test files
* Common testing file patterns
* Testing configuration
* Testing framework indicators

**Status:** 🟡 Implemented / Being Improved

The testing score and details are now part of the analysis structure, with additional checks planned.

---

## Phase 9 — Code Structure Analysis

**Goal:** Evaluate how well the repository is organized.

### Current Checks

The analyzer now checks:

* Common project folders
* Source file count
* Configuration files
* Repository subdirectories
* Overall file organization

### Detected Project Folders

Examples include:

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

Examples include:

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

### Analysis Details

The analyzer returns descriptive messages such as:

```text
Organized project folders detected.
10 source files detected.
Project configuration files detected.
Repository contains organized subdirectories.
```

The API now returns Code Structure in the following format:

```json
{
  "code_structure": {
    "score": 15,
    "details": [
      {
        "type": "success",
        "message": "Organized project folders detected."
      },
      {
        "type": "success",
        "message": "Project configuration files detected."
      }
    ]
  }
}
```

**Status:** ✅ Implemented and being tested

---

## Phase 10 — Security Analysis

**Goal:** Detect potential security issues and security-related project practices.

### Planned Checks

* Sensitive files
* Environment files
* Security configuration
* Dependency information
* Security-related patterns
* Bandit analysis for Python projects

**Status:** 🟡 Basic scoring implemented; advanced analysis planned

---

## Phase 11 — Maintainability Analysis

**Goal:** Evaluate factors that affect long-term project maintenance.

### Planned Checks

* Code organization
* Project complexity
* File structure
* Configuration
* Documentation
* Code quality
* Dependency management

Future versions may integrate tools such as Radon for Python complexity analysis.

**Status:** 🟡 Basic scoring implemented; advanced analysis planned

---

## Phase 12 — Health Scoring Engine

**Goal:** Combine individual analysis categories into an overall health score.

### Planned Structure

```text
Documentation
      |
Testing
      |
Code Structure
      |
Security
      |
Maintainability
      |
      v
Overall Health Score / 100
```

The scoring engine currently contains individual category calculations.

**Status:** 🟡 In Progress

---

## Phase 13 — Recommendations

**Goal:** Provide useful suggestions based on detected repository issues.

### Planned Recommendations

* Add or improve README documentation
* Increase testing support
* Improve project organization
* Add missing configuration files
* Improve dependency management
* Reduce code complexity
* Address security issues
* Improve maintainability

**Status:** ⏳ Pending

---

## Phase 14 — React + FastAPI Integration

**Goal:** Connect the completed backend analysis system with the React frontend.

### Tasks

* Configure CORS
* Send repository URL from React
* Call `POST /analyze`
* Receive JSON response
* Handle loading state
* Handle API errors
* Display repository information
* Display category scores
* Display analysis details

**Status:** ⏳ Next Major Step

---

## Phase 15 — Dashboard and Visualization

**Goal:** Present the repository analysis clearly through a dashboard.

### Planned Dashboard

* Overall health score
* Documentation score
* Testing score
* Code Structure score
* Security score
* Maintainability score
* Analysis details
* Repository statistics
* Charts
* Detected issues
* Recommendations

**Status:** ⏳ Pending

---

## Phase 16 — Database and History

**Goal:** Store previous repository analyses.

### Planned Features

* PostgreSQL database
* Analysis history
* Repository history
* Score changes over time
* Previous reports
* Repository comparison

**Status:** ⏳ Future Phase

---

## Phase 17 — Advanced Features

Possible future features:

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

The project currently follows this structure:

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

## Frontend Progress

The React/Vite project has been created successfully.

### Implemented

* React + Vite setup
* `App.jsx`
* `Navbar.jsx`
* `Home.jsx`
* Basic application structure
* Repository URL input
* React state using `useState`
* Analyze Repository button

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
Display analysis results
```

The frontend is now ready for the next stage of backend API integration and result visualization.

---

# Backend Progress

The FastAPI backend has been created successfully.

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
* GET `/`
* POST `/analyze`
* GitHub URL validation
* GitHub username/repository extraction
* GitHub API request structure
* Repository information retrieval
* Documentation scoring
* Testing scoring
* Code Structure scoring
* Code Structure analysis details
* Basic security scoring
* Maintainability scoring

---

## Current Backend Flow

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

## Current Code Structure Analysis Flow

The Code Structure analyzer now performs several checks:

```text
Repository Files
      |
      +----> Project Folders
      |
      +----> Source Files
      |
      +----> Configuration Files
      |
      +----> Directory Organization
      |
      v
Code Structure Score
      +
Analysis Details
```

This allows the backend to return both a numerical score and human-readable explanations.

---

## API Response Structure

The `/analyze` endpoint is being developed toward a response similar to:

```json
{
  "message": "Repository analyzed successfully",
  "repository": {
    "name": "Github-Health-Analyze"
  },
  "health_score": {
    "documentation": {
      "score": 20,
      "details": []
    },
    "testing": {
      "score": 0,
      "details": []
    },
    "code_structure": {
      "score": 15,
      "details": []
    },
    "security": {
      "score": 10,
      "details": []
    },
    "maintainability": 15
  }
}
```

The exact scores depend on the repository being analyzed.

---

# Current Development Status

### Completed

* ✅ React/Vite project setup
* ✅ Basic frontend UI
* ✅ Repository URL input
* ✅ FastAPI backend
* ✅ GitHub URL validation
* ✅ GitHub API integration structure
* ✅ Repository information retrieval
* ✅ Documentation analysis
* ✅ Testing analysis foundation
* ✅ Code Structure scoring
* ✅ Code Structure detail analysis
* ✅ Basic security analysis
* ✅ Maintainability scoring

### Currently Working On

* 🔄 Testing and improving repository analysis
* 🔄 Connecting React frontend with FastAPI
* 🔄 Displaying analysis results in the frontend
* 🔄 Improving scoring accuracy

### Next Immediate Step

The next step is to update **`Home.jsx`** so the React dashboard can display:

```text
Code Structure Score
        |
        +---- Score
        |
        +---- Analysis Details
        |
        +---- Success Messages
        |
        +---- Warning Messages
```

After that, the remaining analysis categories can be connected to the frontend in the same way.

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

**Backend repository analysis is now being built category-by-category.**

The latest completed development step is the **Code Structure Analysis Details** module. The next development step is to connect these backend results to the React `Home.jsx` interface.