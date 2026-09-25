# GitHub Repository Health Analyzer

## Part 1 --- Project Description

### Overview

**GitHub Repository Health Analyzer** is a web-based application
designed to evaluate the overall health and quality of a GitHub
repository.

The user provides a GitHub repository URL, for example:

`https://github.com/username/repository`

The application will collect repository information through the GitHub
API, analyze the project, calculate a health score, and present the
results through a React dashboard.

### Main Goal

The main goal of the project is to help developers quickly understand
the quality, maintainability, documentation, testing, structure, and
security condition of a GitHub repository.

### Planned Health Metrics

The project will calculate an overall Repository Health Score out of 100
using areas such as:

-   **Documentation**
-   **Testing**
-   **Code Structure**
-   **Security**
-   **Maintainability**

Additional analysis will be added as the project develops.

### Technology Stack

**Frontend** - React - Vite - JavaScript - CSS - Recharts (planned for
charts)

**Backend** - Python - FastAPI - Uvicorn - HTTPX

**External API** - GitHub REST API

**Planned Analysis Tools** - Radon for Python code complexity - Bandit
for Python security analysis - GitHub repository and commit data -
Dependency analysis

**Planned Database** - PostgreSQL

### Basic Architecture

``` text
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
Score Calculation Engine
  |
  v
JSON Analysis Result
  |
  v
React Dashboard
```

------------------------------------------------------------------------

# Part 2 --- Project Roadmap

## Phase 1 --- React Project Setup

**Goal:** Create the frontend foundation.

Tasks: - Create React project using Vite - Install dependencies -
Understand Vite project structure - Configure the main React files -
Create the basic application structure

**Status:** Completed

------------------------------------------------------------------------

## Phase 2 --- Frontend UI

**Goal:** Build the basic user interface.

Tasks: - Create Navbar - Create Home page - Add project title and
description - Add repository URL input - Create Analyze Repository
button - Improve layout and styling

**Status:** Basic structure completed; UI improvements can continue.

------------------------------------------------------------------------

## Phase 3 --- Frontend Interactivity

**Goal:** Make the React interface functional.

Tasks: - Use React `useState` - Handle repository URL input - Handle
button click - Validate user input - Add loading state - Add error
messages - Prepare API request - Display backend results

**Status:** Started. Repository URL state/input handling has been
implemented.

------------------------------------------------------------------------

## Phase 4 --- FastAPI Backend

**Goal:** Create the backend API.

Tasks: - Create Python backend folder - Create virtual environment -
Install FastAPI, Uvicorn and HTTPX - Create `main.py` - Create GET `/`
endpoint - Create POST `/analyze` endpoint - Validate repository URLs -
Add Pydantic request model - Connect backend to GitHub API

**Status:** Mostly completed. FastAPI server and repository URL
validation are working. GitHub API integration has been created and is
being debugged.

------------------------------------------------------------------------

## Phase 5 --- Connect React and FastAPI

**Goal:** Connect the frontend with the backend.

Tasks: - Configure CORS - Send repository URL from React to FastAPI -
Receive JSON response - Handle loading and errors - Display repository
information in React

**Status:** Pending

------------------------------------------------------------------------

## Phase 6 --- GitHub API Integration

**Goal:** Collect detailed repository information.

Planned data: - Repository name - Full repository name - Description -
Primary language - Stars - Forks - Open issues - Default branch -
Repository metadata - File tree - README information - Commit/activity
information

**Status:** Integration code created. Initial testing exposed a
response/JSON parsing issue that still needs to be resolved.

------------------------------------------------------------------------

## Phase 7 --- Repository Code Analysis

**Goal:** Analyze the actual contents of a repository.

Planned analysis: - File and folder structure - Programming languages -
Lines of code - Documentation files - Test files - Configuration files -
Dependency files - Code complexity - Security patterns - Project
organization

**Status:** Pending

------------------------------------------------------------------------

## Phase 8 --- Health Scoring Engine

**Goal:** Convert analysis results into a health score.

Planned categories:

``` text
Documentation
Testing
Code Structure
Security
Maintainability
        |
        v
Overall Health Score / 100
```

The scoring rules will be defined after the repository analysis modules
are implemented.

**Status:** Pending

------------------------------------------------------------------------

## Phase 9 --- Recommendations

**Goal:** Give useful suggestions based on detected problems.

Examples: - Add or improve README documentation - Increase test
coverage - Reduce code complexity - Add dependency management - Fix
security issues - Improve project structure - Add missing configuration
files

**Status:** Pending

------------------------------------------------------------------------

## Phase 10 --- Dashboard and Visualization

**Goal:** Present analysis results clearly.

Planned dashboard: - Overall health score - Category scores - Charts -
Repository statistics - Detected issues - Recommendations - File/code
analysis summary

**Status:** Pending

------------------------------------------------------------------------

## Phase 11 --- Database and History

**Goal:** Store previous analyses.

Planned features: - PostgreSQL database - Analysis history - Repository
history - Score changes over time - Previous reports - Repository
comparison

**Status:** Pending

------------------------------------------------------------------------

## Phase 12 --- Advanced Features

Possible future features: - AI-generated recommendations - Dependency
health analysis - Git activity analysis - Repository comparison - PDF
reports - Score history charts - Authentication - Saved repositories -
Deployment

**Status:** Future scope

------------------------------------------------------------------------

# Part 3 --- Current Progress

## Current Project Structure

The project currently follows this structure:

``` text
github-health-analyzer/
│
├── .gitignore
│
├── backend/
│   ├── main.py
│   ├── github_api.py
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

## Frontend Progress

The React/Vite project has been created successfully.

Implemented:

-   React + Vite setup
-   `App.jsx`
-   `Navbar.jsx`
-   `Home.jsx`
-   Basic application structure
-   Repository URL input
-   React state using `useState`
-   Analyze Repository button

Example frontend flow:

``` text
User enters GitHub URL
        |
        v
React stores URL in state
        |
        v
Analyze Repository button
        |
        v
Backend API request (planned/next)
```

## Backend Progress

The FastAPI backend has been created successfully.

Implemented:

-   Python virtual environment
-   FastAPI
-   Uvicorn
-   HTTPX
-   Pydantic
-   `main.py`
-   `github_api.py`
-   `requirements.txt`
-   GET `/`
-   POST `/analyze`
-   GitHub URL validation
-   GitHub username/repository extraction
-   GitHub API request structure

The backend server successfully starts at:

`http://127.0.0.1:8000`

FastAPI Swagger documentation is available at:

`http://127.0.0.1:8000/docs`

## Current Backend Flow

``` text
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
Return JSON response
```

## Current Issue

During GitHub API testing, the application reached the GitHub API
request successfully, but the response caused a JSON parsing error at:

``` python
response.json()
```

The `github_api.py` file has since been made safer by: - Adding GitHub
request headers - Adding a timeout - Handling HTTP status codes -
Checking the response before parsing - Catching invalid JSON responses -
Printing response status/content type for debugging

The next development step is to complete the GitHub API debugging and
confirm that `/analyze` returns repository information successfully.

## Git Repository Status

The project was previously connected to a GitHub repository, but that
remote repository was deleted to allow the project to be restarted
cleanly.

There was also an unfinished Git rebase involving conflicts in: -
`.gitignore` - `src/components/Home.jsx` - `src/components/Navbar.jsx`

The local project files are being cleaned up before creating a new
GitHub repository.

## Current Next Steps

1.  Finish cleaning the local Git/rebase state.
2.  Keep only the project-level `.gitignore`.
3.  Keep the backend virtual environment at `backend/venv`.
4.  Verify the FastAPI GitHub API integration.
5.  Create a fresh GitHub repository.
6.  Push the clean project to GitHub.
7.  Continue with CORS and React → FastAPI connection.
8.  Start repository file/code analysis.
9.  Build the scoring engine.
10. Build the final health dashboard.

------------------------------------------------------------------------

## Project Development Principle

The project is being developed incrementally. Each phase should be
completed and tested before moving to the next phase.

The target final workflow is:

``` text
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
 Repository Data + Code
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
```
