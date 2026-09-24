import httpx


async def get_repository_info(username: str, repository: str):

    url = f"https://api.github.com/repos/{username}/{repository}"

    headers = {
        "Accept": "application/vnd.github+json",
        "User-Agent": "GitHub-Health-Analyzer"
    }

    async with httpx.AsyncClient(timeout=15.0) as client:
        response = await client.get(url, headers=headers)

    # Repository does not exist
    if response.status_code == 404:
        return None

    # GitHub rate limit
    if response.status_code == 403:
        return {
            "error": "GitHub API rate limit reached. Please try again later."
        }

    # Any other unsuccessful response
    if response.status_code != 200:
        return {
            "error": f"GitHub API returned status code {response.status_code}"
        }

    # Make sure GitHub actually returned JSON
    content_type = response.headers.get("content-type", "")

    if "application/json" not in content_type:
        return {
            "error": "GitHub API did not return JSON data."
        }

    data = response.json()

    return {
        "name": data.get("name"),
        "full_name": data.get("full_name"),
        "description": data.get("description"),
        "language": data.get("language"),
        "stars": data.get("stargazers_count"),
        "forks": data.get("forks_count"),
        "open_issues": data.get("open_issues_count"),
        "default_branch": data.get("default_branch")
    }