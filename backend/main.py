
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from urllib.parse import urlparse

from github_api import (
    get_repository_info,
    get_readme,
    get_repository_contents
)

from health_analyzer import (
    calculate_documentation_score,
    calculate_testing_score,
    calculate_code_structure_score,
    calculate_security_score,
    calculate_maintainability_score
)


app = FastAPI()


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


class RepositoryRequest(BaseModel):
    repo_url: str


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
            detail="GitHub URL must be in the format: https://github.com/username/repository"
        )

    return {
        "username": path_parts[0],
        "repository": path_parts[1]
    }


@app.get("/")
def home():

    return {
        "message": "GitHub Health Analyzer API is running"
    }


@app.post("/analyze")
async def analyze_repository(request: RepositoryRequest):

    github_info = validate_github_url(request.repo_url)

    username = github_info["username"]
    repository_name = github_info["repository"]

    repository_info = await get_repository_info(
        username,
        repository_name
    )

    if repository_info is None:
        raise HTTPException(
            status_code=404,
            detail="GitHub repository not found."
        )

    readme_content = await get_readme(
        username,
        repository_name
    )

    documentation_score = calculate_documentation_score(
        repository_info,
        readme_content
    )

    repository_files = await get_repository_contents(
        username,
        repository_name
    )

    testing_score = calculate_testing_score(
        repository_files
    )

    code_structure_score = calculate_code_structure_score(
        repository_files
    )

    security_score = calculate_security_score(
        repository_files
    )

    maintainability_score = calculate_maintainability_score(
        repository_files
    )

    return {
        "message": "Repository analyzed successfully",
        "repository_url": request.repo_url,
        "repository": repository_info,
        "health_score": {
            "documentation": documentation_score,
            "testing": testing_score,
            "code_structure": code_structure_score,
            "security": security_score,
            "maintainability": maintainability_score
        }
    }

