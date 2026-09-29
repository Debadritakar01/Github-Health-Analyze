from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from urllib.parse import urlparse

from github_api import (
    get_repository_info,
    get_readme,
    get_repository_contents,
    get_file_content
)

from health_analyzer import (
    calculate_documentation_score,
    get_documentation_details,

    calculate_testing_score,
    get_testing_details,

    calculate_code_structure_score,
    get_code_structure_details,

    calculate_security_score,
    get_security_details,

    calculate_maintainability_score,
    get_maintainability_details
)


app = FastAPI()


# CORS configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://localhost:5174",
        "http://127.0.0.1:5173",
        "http://127.0.0.1:5174",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Request model
class RepositoryRequest(BaseModel):
    repo_url: str


# Validate GitHub repository URL
def validate_github_url(repo_url: str):

    parsed_url = urlparse(repo_url)

    if parsed_url.netloc != "github.com":
        raise HTTPException(
            status_code=400,
            detail="Please enter a valid GitHub repository URL."
        )

    path_parts = parsed_url.path.strip("/").split("/")

    if len(path_parts) != 2:
        raise HTTPException(
            status_code=400,
            detail=(
                "GitHub URL must be in the format: "
                "https://github.com/username/repository"
            )
        )

    return {
        "username": path_parts[0],
        "repository": path_parts[1]
    }


# Home endpoint
@app.get("/")
def home():

    return {
        "message": "GitHub Health Analyzer API is running"
    }


# Repository analysis endpoint
@app.post("/analyze")
async def analyze_repository(request: RepositoryRequest):

    # Validate GitHub URL
    github_info = validate_github_url(request.repo_url)

    username = github_info["username"]
    repository_name = github_info["repository"]


    # Get repository information
    repository_info = await get_repository_info(
        username,
        repository_name
    )

    if repository_info is None:
        raise HTTPException(
            status_code=404,
            detail="GitHub repository not found."
        )


    # Get README content
    readme_content = await get_readme(
        username,
        repository_name
    )


    # -----------------------------
    # Documentation Analysis
    # -----------------------------

    documentation_score = calculate_documentation_score(
        repository_info,
        readme_content
    )

    documentation_details = get_documentation_details(
        repository_info,
        readme_content
    )


    # Get repository files
    repository_files = await get_repository_contents(
        username,
        repository_name
    )
    package_content = await get_file_content(
        username,
        repository,
        "package.json"
    )


    # -----------------------------
    # Testing Analysis
    # -----------------------------

    testing_score = calculate_testing_score(
    repository_files,
    package_content
   )

    testing_details = get_testing_details(
        repository_files,
        package_content
    )


    # -----------------------------
    # Code Structure Analysis
    # -----------------------------

    code_structure_score = calculate_code_structure_score(
        repository_files
    )

    code_structure_details = get_code_structure_details(
        repository_files
    )


    # -----------------------------
    # Security Analysis
    # -----------------------------

    security_score = calculate_security_score(
        repository_files
    )

    security_details = get_security_details(
        repository_files
    )


    # -----------------------------
    # Maintainability Analysis
    # -----------------------------

    maintainability_score = calculate_maintainability_score(
        repository_files
    )

    maintainability_details = get_maintainability_details(
        repository_files
    )


    # -----------------------------
    # Overall Health Score
    # -----------------------------

    overall_score = (
        documentation_score
        + testing_score
        + code_structure_score
        + security_score
        + maintainability_score
    )


    # -----------------------------
    # Return Analysis Result
    # -----------------------------

    return {
        "message": "Repository analyzed successfully",

        "repository_url": request.repo_url,

        "repository": repository_info,

        "health_score": {

            "overall": overall_score,

            "documentation": {
                "score": documentation_score,
                "details": documentation_details
            },

            "testing": {
                "score": testing_score,
                "details": testing_details
            },

            "code_structure": {
                "score": code_structure_score,
                "details": code_structure_details
            },

            "security": {
                "score": security_score,
                "details": security_details
            },

            "maintainability": {
                "score": maintainability_score,
                "details": maintainability_details
            }
        }
    }

