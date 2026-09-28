def calculate_documentation_score(repository_info, readme_content):
    score = 0

    if not repository_info:
        return score

    if readme_content:
        score += 10

    if repository_info.get("description"):
        score += 5

    if repository_info.get("language"):
        score += 5

    return min(score, 20)


def get_documentation_details(repository_info, readme_content):
    details = []

    if readme_content:
        details.append({
            "type": "success",
            "message": "README file found."
        })
    else:
        details.append({
            "type": "warning",
            "message": "README file not found."
        })

    if repository_info.get("description"):
        details.append({
            "type": "success",
            "message": "Repository description found."
        })
    else:
        details.append({
            "type": "warning",
            "message": "Repository description is missing."
        })

    if repository_info.get("language"):
        details.append({
            "type": "success",
            "message": "Primary programming language detected."
        })
    else:
        details.append({
            "type": "warning",
            "message": "Programming language could not be detected."
        })

    return details


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


def get_testing_details(repository_files):
    details = []

    if not repository_files:
        details.append({
            "type": "warning",
            "message": "Repository files could not be analyzed."
        })
        return details

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
        details.append({
            "type": "success",
            "message": "Testing directory found."
        })
    else:
        details.append({
            "type": "warning",
            "message": "No dedicated testing directory found."
        })

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
        details.append({
            "type": "success",
            "message": "Testing framework detected."
        })
    else:
        details.append({
            "type": "warning",
            "message": "No recognized testing framework detected."
        })

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
        details.append({
            "type": "success",
            "message": f"{len(test_files)} test files detected."
        })
    elif len(test_files) == 1:
        details.append({
            "type": "warning",
            "message": "Only one test file detected."
        })
    else:
        details.append({
            "type": "warning",
            "message": "No test files detected."
        })

    return details


def calculate_code_structure_score(repository_files):
    score = 0

    if not repository_files:
        return score

    # Extract file paths safely
    file_paths = [
        item.get("path", "").lower().strip("/")
        for item in repository_files
        if isinstance(item, dict)
    ]

    # Remove empty paths
    file_paths = [path for path in file_paths if path]

    if not file_paths:
        return score

    
    important_folders = [
        "src",
        "app",
        "components",
        "backend",
        "frontend",
        "api",
        "utils",
        "services",
        "models",
        "controllers",
    ]

    folders_found = 0

    for folder in important_folders:
        folder_exists = any(
            path.startswith(folder + "/") or f"/{folder}/" in path
            for path in file_paths
        )

        if folder_exists:
            folders_found += 1

    if folders_found >= 4:
        score += 8
    elif folders_found >= 2:
        score += 5
    elif folders_found == 1:
        score += 3

    
    source_extensions = (
        ".py",
        ".js",
        ".jsx",
        ".ts",
        ".tsx",
        ".java",
        ".cpp",
        ".c",
        ".cs",
        ".go",
        ".php",
    )

    source_files = [
        path
        for path in file_paths
        if path.endswith(source_extensions)
    ]

    if len(source_files) >= 10:
        score += 4
    elif len(source_files) >= 5:
        score += 3
    elif len(source_files) >= 2:
        score += 2

   
    configuration_files = [
        "package.json",
        "requirements.txt",
        "pyproject.toml",
        "pom.xml",
        "build.gradle",
        "vite.config.js",
        "vite.config.ts",
        "tsconfig.json",
    ]

    config_found = any(
        path.split("/")[-1] in configuration_files
        for path in file_paths
    )

    if config_found:
        score += 3

    
    root_files = [
        path
        for path in file_paths
        if "/" not in path
    ]

    nested_files = [
        path
        for path in file_paths
        if "/" in path
    ]

    if len(file_paths) > 5 and len(nested_files) > 0:
        score += 3

    return min(score, 20)


def calculate_security_score(repository_files):
    score = 0

    if not repository_files:
        return score

    file_paths = [
        item.get("path", "").lower()
        for item in repository_files
    ]

    security_files = [
        ".gitignore",
        ".env.example",
        "security.md",
        "security.txt"
    ]

    for security_file in security_files:
        if security_file in file_paths:
            score += 5

    return min(score, 20)
def get_code_structure_details(repository_files):
    details = []

    if not repository_files:
        details.append({
            "type": "warning",
            "message": "Repository files could not be analyzed."
        })
        return details

    # Extract file paths safely
    file_paths = [
        item.get("path", "").lower().strip("/")
        for item in repository_files
        if isinstance(item, dict)
    ]

    # Remove empty paths
    file_paths = [
        path for path in file_paths
        if path
    ]

    if not file_paths:
        details.append({
            "type": "warning",
            "message": "No repository files were found."
        })
        return details


    important_folders = [
        "src",
        "app",
        "components",
        "backend",
        "frontend",
        "api",
        "utils",
        "services",
        "models",
        "controllers"
    ]

    folders_found = [
        folder
        for folder in important_folders
        if any(
            path.startswith(folder + "/")
            or f"/{folder}/" in path
            for path in file_paths
        )
    ]

    if len(folders_found) >= 4:
        details.append({
            "type": "success",
            "message": (
                f"Well-organized project structure detected "
                f"({len(folders_found)} common folders)."
            )
        })

    elif len(folders_found) >= 2:
        details.append({
            "type": "success",
            "message": (
                f"Organized project folders detected "
                f"({len(folders_found)})."
            )
        })

    elif len(folders_found) == 1:
        details.append({
            "type": "warning",
            "message": (
                f"Only one common project organization folder detected: "
                f"{folders_found[0]}."
            )
        })

    else:
        details.append({
            "type": "warning",
            "message": "No common project organization folders detected."
        })

    # --------------------------------------------------
    # 2. Check source/code files
    # --------------------------------------------------
    source_extensions = (
        ".py",
        ".js",
        ".jsx",
        ".ts",
        ".tsx",
        ".java",
        ".cpp",
        ".c",
        ".cs",
        ".go",
        ".php"
    )

    source_files = [
        path
        for path in file_paths
        if path.endswith(source_extensions)
    ]

    source_count = len(source_files)

    if source_count >= 10:
        details.append({
            "type": "success",
            "message": f"{source_count} source files detected."
        })

    elif source_count >= 5:
        details.append({
            "type": "success",
            "message": f"{source_count} source files detected."
        })

    elif source_count >= 2:
        details.append({
            "type": "warning",
            "message": f"Only {source_count} source files detected."
        })

    else:
        details.append({
            "type": "warning",
            "message": "Very few source files detected."
        })

    # --------------------------------------------------
    # 3. Check configuration/project files
    # --------------------------------------------------
    configuration_files = [
        "package.json",
        "requirements.txt",
        "pyproject.toml",
        "pom.xml",
        "build.gradle",
        "vite.config.js",
        "vite.config.ts",
        "tsconfig.json",
        "dockerfile",
        "docker-compose.yml",
        "docker-compose.yaml",
        ".env.example"
    ]

    config_found = [
        file_name
        for file_name in configuration_files
        if any(
            path.split("/")[-1] == file_name
            for path in file_paths
        )
    ]

    if config_found:
        details.append({
            "type": "success",
            "message": (
                f"Project configuration files detected "
                f"({len(config_found)})."
            )
        })

    else:
        details.append({
            "type": "warning",
            "message": (
                "No common project configuration files detected."
            )
        })

    # --------------------------------------------------
    # 4. Check directory organization
    # --------------------------------------------------
    root_files = [
        path
        for path in file_paths
        if "/" not in path
    ]

    nested_files = [
        path
        for path in file_paths
        if "/" in path
    ]

    if len(file_paths) > 5 and len(nested_files) > 0:
        details.append({
            "type": "success",
            "message": (
                f"Repository contains organized subdirectories "
                f"({len(nested_files)} nested files)."
            )
        })

    elif len(file_paths) <= 5:
        details.append({
            "type": "warning",
            "message": (
                "Repository is small, so directory organization "
                "could not be fully evaluated."
            )
        })

    else:
        details.append({
            "type": "warning",
            "message": (
                f"Most repository files are located in the root directory "
                f"({len(root_files)} root files)."
            )
        })

    return details


def get_security_details(repository_files):
    details = []

    if not repository_files:
        details.append({
            "type": "warning",
            "message": "Repository files could not be analyzed."
        })
        return details

    file_paths = [
        item.get("path", "").lower()
        for item in repository_files
    ]

    if ".gitignore" in file_paths:
        details.append({
            "type": "success",
            "message": ".gitignore file found."
        })
    else:
        details.append({
            "type": "warning",
            "message": ".gitignore file not found."
        })

    if ".env.example" in file_paths:
        details.append({
            "type": "success",
            "message": ".env.example file found."
        })
    else:
        details.append({
            "type": "warning",
            "message": ".env.example file not found."
        })

    sensitive_files = [
        ".env",
        "credentials.json",
        "secrets.json",
        "config.json"
    ]

    sensitive_found = [
        file
        for file in sensitive_files
        if file in file_paths
    ]

    if sensitive_found:
        details.append({
            "type": "warning",
            "message": "Potential sensitive configuration files detected."
        })
    else:
        details.append({
            "type": "success",
            "message": "No obvious sensitive configuration files detected."
        })

    return details


def calculate_maintainability_score(repository_files):
    score = 0

    if not repository_files:
        return score

    file_paths = [
        item.get("path", "").lower()
        for item in repository_files
    ]

    if "readme.md" in file_paths:
        score += 5

    if ".gitignore" in file_paths:
        score += 5

    documentation_files = [
        path
        for path in file_paths
        if path.endswith(".md")
    ]

    if len(documentation_files) >= 2:
        score += 5

    if len(file_paths) > 10:
        score += 5

    return min(score, 20)


# ---------------------------------------------------------
# TEST DATA
# ---------------------------------------------------------

if __name__ == "__main__":

    repository_info = {
        "description": "GitHub Repository Health Analyzer",
        "language": "Python"
    }

    readme_content = """
    # GitHub Health Analyzer

    An application that analyzes GitHub repositories
    and calculates their overall health score.
    """

    repository_files = [
        {"path": "README.md"},
        {"path": ".gitignore"},
        {"path": ".env.example"},
        {"path": "backend/main.py"},
        {"path": "backend/api.py"},
        {"path": "backend/services/github.py"},
        {"path": "frontend/src/App.jsx"},
        {"path": "frontend/src/components/Dashboard.jsx"},
        {"path": "tests/test_api.py"},
        {"path": "tests/test_github.py"},
        {"path": "requirements.txt"},
        {"path": "SECURITY.md"}
    ]

    documentation_score = calculate_documentation_score(
        repository_info,
        readme_content
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

    total_score = (
        documentation_score
        + testing_score
        + code_structure_score
        + security_score
        + maintainability_score
    )

    print("=" * 50)
    print("       GITHUB REPOSITORY HEALTH ANALYZER")
    print("=" * 50)

    print(f"Documentation Score   : {documentation_score}/20")
    print(f"Testing Score         : {testing_score}/20")
    print(f"Code Structure Score  : {code_structure_score}/20")
    print(f"Security Score        : {security_score}/20")
    print(f"Maintainability Score : {maintainability_score}/20")

    print("-" * 50)
    print(f"TOTAL HEALTH SCORE    : {total_score}/100")
    print("=" * 50)

    print("\nDocumentation Details:")
    for detail in get_documentation_details(
        repository_info,
        readme_content
    ):
        print(f"[{detail['type'].upper()}] {detail['message']}")

    print("\nTesting Details:")
    for detail in get_testing_details(repository_files):
        print(f"[{detail['type'].upper()}] {detail['message']}")

    print("\nSecurity Details:")
    for detail in get_security_details(repository_files):
        print(f"[{detail['type'].upper()}] {detail['message']}")