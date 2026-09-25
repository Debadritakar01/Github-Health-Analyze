def calculate_documentation_score(repository, readme_content=None):
    score = 0

    if repository.get("description"):
        score += 5

    if readme_content:
        score += 10

        readme_lower = readme_content.lower()

        useful_sections = [
            "installation",
            "usage",
            "features",
            "technologies",
            "contributing"
        ]

        section_count = sum(
            1
            for section in useful_sections
            if section in readme_lower
        )

        score += min(section_count, 5)

    return min(score, 20)


def calculate_testing_score(repository_files):
    score = 0

    if not repository_files:
        return score

    file_paths = [
        item.get("path", "").lower()
        for item in repository_files
    ]

    testing_folders = [
        "test/",
        "tests/",
        "__tests__/"
    ]

    has_testing_folder = any(
        any(path.startswith(folder) for folder in testing_folders)
        for path in file_paths
    )

    if has_testing_folder:
        score += 10

    testing_frameworks = [
        "pytest",
        "jest",
        "vitest",
        "mocha",
        "junit",
        "unittest"
    ]

    framework_found = any(
        any(framework in path for framework in testing_frameworks)
        for path in file_paths
    )

    if framework_found:
        score += 5

    test_files = [
        path
        for path in file_paths
        if (
            "test_" in path
            or "_test." in path
            or ".test." in path
            or ".spec." in path
        )
    ]

    if len(test_files) >= 2:
        score += 5

    return min(score, 20)


def calculate_code_structure_score(repository_files):
    score = 0

    if not repository_files:
        return score

    file_paths = [
        item.get("path", "").lower()
        for item in repository_files
    ]

    source_folders = [
        "src/",
        "app/",
        "backend/",
        "frontend/",
        "lib/",
        "components/"
    ]

    has_source_folder = any(
        any(path.startswith(folder) for folder in source_folders)
        for path in file_paths
    )

    if has_source_folder:
        score += 5

    has_frontend = any(
        path.startswith("frontend/")
        for path in file_paths
    )

    has_backend = any(
        path.startswith("backend/")
        for path in file_paths
    )

    if has_frontend and has_backend:
        score += 5

    config_files = [
        "package.json",
        "requirements.txt",
        "pyproject.toml",
        "vite.config.js",
        "vite.config.jsx",
        "tsconfig.json"
    ]

    has_config_file = any(
        path.split("/")[-1] in config_files
        for path in file_paths
    )

    if has_config_file:
        score += 3

    root_files = [
        path
        for path in file_paths
        if "/" not in path
    ]

    if len(root_files) <= 10:
        score += 3

    folders = set()

    for path in file_paths:
        if "/" in path:
            folders.add(path.split("/")[0])

    if len(folders) >= 2:
        score += 2

    return min(score, 20)
def calculate_security_score(repository_files):
    score = 0

    if not repository_files:
        return score

    file_paths = [
        item.get("path", "").lower()
        for item in repository_files
    ]

    # 1. Check for environment files
    env_files = [
        ".env",
        ".env.example"
    ]

    has_env_file = any(
        path.split("/")[-1] in env_files
        for path in file_paths
    )

    if has_env_file:
        score += 5

    # 2. Check for security-related configuration
    security_files = [
        "security.md",
        "security.txt",
        ".github/dependabot.yml",
        ".github/dependabot.yaml"
    ]

    has_security_file = any(
        path in security_files
        for path in file_paths
    )

    if has_security_file:
        score += 5

    # 3. Check for GitHub workflows
    has_github_workflows = any(
        path.startswith(".github/workflows/")
        for path in file_paths
    )

    if has_github_workflows:
        score += 5

    # 4. Check for dependency files
    dependency_files = [
        "package.json",
        "requirements.txt",
        "package-lock.json",
        "yarn.lock",
        "pipfile",
        "poetry.lock"
    ]

    has_dependency_file = any(
        path.split("/")[-1] in dependency_files
        for path in file_paths
    )

    if has_dependency_file:
        score += 5

    return min(score, 20)
def calculate_maintainability_score(repository_files):
    score = 0

    if not repository_files:
        return score

    file_paths = [
        item.get("path", "").lower()
        for item in repository_files
    ]

    # 1. Check for a README file
    has_readme = any(
        path.split("/")[-1] in [
            "readme.md",
            "readme.txt",
            "readme"
        ]
        for path in file_paths
    )

    if has_readme:
        score += 5

    # 2. Check for documentation folder
    has_docs_folder = any(
        path.startswith("docs/")
        for path in file_paths
    )

    if has_docs_folder:
        score += 5

    # 3. Check for configuration/dependency files
    maintainable_files = [
        "package.json",
        "requirements.txt",
        "pyproject.toml",
        "package-lock.json",
        "yarn.lock"
    ]

    has_maintainable_file = any(
        path.split("/")[-1] in maintainable_files
        for path in file_paths
    )

    if has_maintainable_file:
        score += 5

    # 4. Check for GitHub issue templates or contribution guidelines
    has_project_guidelines = any(
        "contributing" in path
        or "issue_template" in path
        or "pull_request_template" in path
        for path in file_paths
    )

    if has_project_guidelines:
        score += 5

    return min(score, 20)