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