from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from urllib.parse import urlparse

from github_api import get_repository_info


app = FastAPI()


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

    repository_info = await get_repository_info(
        github_info["username"],
        github_info["repository"]
    )

    if repository_info is None:

        raise HTTPException(
            status_code=404,
            detail="GitHub repository not found."
        )

    return {
        "message": "Repository found",
        "repository_url": request.repo_url,
        "repository": repository_info
    }