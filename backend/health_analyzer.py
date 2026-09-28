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
        item.get("path", "").lower().strip("/")
        for item in repository_files
        if isinstance(item, dict)
    ]

    # --------------------------------------------------
    # 1. Check for testing directories
    # --------------------------------------------------

    testing_directories = [
        "test/",
        "tests/",
        "__tests__/"
    ]

    has_testing_directory = any(
        path.startswith(directory)
        for path in file_paths
        for directory in testing_directories
    )

    if has_testing_directory:
        score += 8

    # --------------------------------------------------
    # 2. Detect test files
    # --------------------------------------------------

    test_file_patterns = [
        ".test.",
        ".spec.",
        "_test.",
        "test_"
    ]

    test_files = [
        path
        for path in file_paths
        if any(pattern in path for pattern in test_file_patterns)
    ]

    if len(test_files) >= 5:
        score += 7

    elif len(test_files) >= 2:
        score += 5

    elif len(test_files) == 1:
        score += 3

    # --------------------------------------------------
    # 3. Detect testing frameworks
    # --------------------------------------------------

    testing_frameworks = [
        "pytest",
        "jest",
        "vitest",
        "mocha",
        "junit",
        "unittest"
    ]

    framework_detected = any(
        framework in path
        for path in file_paths
        for framework in testing_frameworks
    )

    if framework_detected:
        score += 5

    # Maximum score = 20
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
        item.get("path", "").lower().strip("/")
        for item in repository_files
        if isinstance(item, dict)
    ]

    # --------------------------------------------------
    # Testing directories
    # --------------------------------------------------

    testing_directories = [
        "test/",
        "tests/",
        "__tests__/"
    ]

    detected_directories = [
        directory
        for directory in testing_directories
        if any(
            path.startswith(directory)
            for path in file_paths
        )
    ]

    if detected_directories:
        details.append({
            "type": "success",
            "message": (
                "Testing directory found: "
                + ", ".join(detected_directories)
            )
        })
    else:
        details.append({
            "type": "warning",
            "message": "No dedicated testing directory found."
        })

    # --------------------------------------------------
    # Test files
    # --------------------------------------------------

    test_file_patterns = [
        ".test.",
        ".spec.",
        "_test.",
        "test_"
    ]

    test_files = [
        path
        for path in file_paths
        if any(pattern in path for pattern in test_file_patterns)
    ]

    if test_files:
        details.append({
            "type": "success",
            "message": (
                f"{len(test_files)} test file(s) detected."
            )
        })
    else:
        details.append({
            "type": "warning",
            "message": "No test files detected."
        })

    # --------------------------------------------------
    # Testing frameworks
    # --------------------------------------------------

    testing_frameworks = [
        "pytest",
        "jest",
        "vitest",
        "mocha",
        "junit",
        "unittest"
    ]

    detected_frameworks = [
        framework
        for framework in testing_frameworks
        if any(
            framework in path
            for path in file_paths
        )
    ]

    if detected_frameworks:
        details.append({
            "type": "success",
            "message": (
                "Testing framework detected: "
                + ", ".join(detected_frameworks)
            )
        })
    else:
        details.append({
            "type": "warning",
            "message": "No common testing framework detected."
        })

    return details


def calculate_code_structure_score(repository_files):

    score = 0

    if not repository_files:
        return score

    file_paths = [
        item.get("path", "").lower().strip("/")
        for item in repository_files
        if isinstance(item, dict)
    ]

    # --------------------------------------------------
    # 1. Check project folders
    # --------------------------------------------------

    important_folders = [
        "src/",
        "app/",
        "components/",
        "backend/",
        "frontend/",
        "api/",
        "utils/",
        "services/",
        "models/",
        "controllers/"
    ]

    organized_folders = [
        folder
        for folder in important_folders
        if any(
            path.startswith(folder)
            for path in file_paths
        )
    ]

    folder_count = len(organized_folders)

    if folder_count >= 5:
        score += 7

    elif folder_count >= 3:
        score += 5

    elif folder_count >= 1:
        score += 3

    # --------------------------------------------------
    # 2. Count source files
    # --------------------------------------------------

    source_extensions = (
        ".py",
        ".js",
        ".jsx",
        ".ts",
        ".tsx",
        ".java",
        ".c",
        ".cpp",
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

    if source_count >= 15:
        score += 5

    elif source_count >= 8:
        score += 4

    elif source_count >= 3:
        score += 2

    # --------------------------------------------------
    # 3. Configuration files
    # --------------------------------------------------

    config_files = [
        "package.json",
        "requirements.txt",
        "pyproject.toml",
        "pom.xml",
        "build.gradle",
        "vite.config.js",
        "vite.config.ts",
        "tsconfig.json"
    ]

    detected_configs = [
        config
        for config in config_files
        if config in file_paths
    ]

    if detected_configs:
        score += 4

    # --------------------------------------------------
    # 4. Nested project structure
    # --------------------------------------------------

    nested_files = [
        path
        for path in file_paths
        if "/" in path
    ]

    if len(nested_files) >= 5:
        score += 4

    # Maximum score = 20
    return min(score, 20)


def calculate_security_score(repository_files):

    score = 0

    if not repository_files:
        return score

    file_paths = [
        item.get("path", "").lower().strip("/")
        for item in repository_files
        if isinstance(item, dict)
    ]

    # Security configuration files
    if ".gitignore" in file_paths:
        score += 5

    if ".env.example" in file_paths:
        score += 5

    if "security.md" in file_paths or "security.txt" in file_paths:
        score += 5

    # Check for sensitive files
    sensitive_files = [
        ".env",
        "credentials.json",
        "secrets.json",
        "secret.json",
        "private.key",
        "private.pem"
    ]

    sensitive_files_found = [
        path
        for path in file_paths
        if path in sensitive_files
    ]

    # Give points when no sensitive files are exposed
    if not sensitive_files_found:
        score += 5

    # Reduce score if sensitive files are found
    if sensitive_files_found:
        score -= min(len(sensitive_files_found) * 5, 15)

    return max(0, min(score, 20))
def get_code_structure_details(repository_files):

    details = []

    if not repository_files:
        details.append({
            "type": "warning",
            "message": "Repository files could not be analyzed."
        })
        return details

    file_paths = [
        item.get("path", "").lower().strip("/")
        for item in repository_files
        if isinstance(item, dict)
    ]

    # --------------------------------------------------
    # Project folders
    # --------------------------------------------------

    important_folders = [
        "src/",
        "app/",
        "components/",
        "backend/",
        "frontend/",
        "api/",
        "utils/",
        "services/",
        "models/",
        "controllers/"
    ]

    organized_folders = [
        folder
        for folder in important_folders
        if any(
            path.startswith(folder)
            for path in file_paths
        )
    ]

    if organized_folders:
        details.append({
            "type": "success",
            "message": (
                "Organized folders detected: "
                + ", ".join(organized_folders)
            )
        })
    else:
        details.append({
            "type": "warning",
            "message": "No common project folders detected."
        })

    # --------------------------------------------------
    # Source files
    # --------------------------------------------------

    source_extensions = (
        ".py",
        ".js",
        ".jsx",
        ".ts",
        ".tsx",
        ".java",
        ".c",
        ".cpp",
        ".cs",
        ".go",
        ".php"
    )

    source_files = [
        path
        for path in file_paths
        if path.endswith(source_extensions)
    ]

    details.append({
        "type": "success" if source_files else "warning",
        "message": (
            f"{len(source_files)} source code file(s) detected."
        )
    })

    # --------------------------------------------------
    # Configuration files
    # --------------------------------------------------

    config_files = [
        "package.json",
        "requirements.txt",
        "pyproject.toml",
        "pom.xml",
        "build.gradle",
        "vite.config.js",
        "vite.config.ts",
        "tsconfig.json"
    ]

    detected_configs = [
        config
        for config in config_files
        if config in file_paths
    ]

    if detected_configs:
        details.append({
            "type": "success",
            "message": (
                "Configuration files detected: "
                + ", ".join(detected_configs)
            )
        })
    else:
        details.append({
            "type": "warning",
            "message": "No common configuration files detected."
        })

    # --------------------------------------------------
    # Nested structure
    # --------------------------------------------------

    nested_files = [
        path
        for path in file_paths
        if "/" in path
    ]

    if len(nested_files) >= 5:
        details.append({
            "type": "success",
            "message": (
                f"{len(nested_files)} files are inside directories, "
                "indicating organized project structure."
            )
        })
    else:
        details.append({
            "type": "warning",
            "message": "Limited directory nesting detected."
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
        item.get("path", "").lower().strip("/")
        for item in repository_files
        if isinstance(item, dict)
    ]

    # Check .gitignore
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

    # Check .env.example
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

    # Check security documentation
    security_docs = [
        "security.md",
        "security.txt"
    ]

    if any(path in file_paths for path in security_docs):
        details.append({
            "type": "success",
            "message": "Security documentation found."
        })
    else:
        details.append({
            "type": "warning",
            "message": "Security documentation not found."
        })

    # Check sensitive files
    sensitive_files = [
        ".env",
        "credentials.json",
        "secrets.json",
        "secret.json",
        "private.key",
        "private.pem"
    ]

    sensitive_files_found = [
        path
        for path in file_paths
        if path in sensitive_files
    ]

    if sensitive_files_found:
        details.append({
            "type": "warning",
            "message": (
                "Potentially sensitive files detected: "
                + ", ".join(sensitive_files_found)
            )
        })
    else:
        details.append({
            "type": "success",
            "message": "No common sensitive files detected."
        })

    return details


def calculate_maintainability_score(repository_files):

    score = 0

    if not repository_files:
        return score

    file_paths = [
        item.get("path", "").lower().strip("/")
        for item in repository_files
        if isinstance(item, dict)
    ]

    # --------------------------------------------------
    # 1. README
    # --------------------------------------------------

    if "readme.md" in file_paths:
        score += 5

    # --------------------------------------------------
    # 2. Git ignore
    # --------------------------------------------------

    if ".gitignore" in file_paths:
        score += 5

    # --------------------------------------------------
    # 3. Documentation
    # --------------------------------------------------

    documentation_files = [
        path
        for path in file_paths
        if path.endswith(".md")
    ]

    if len(documentation_files) >= 2:
        score += 5

    # --------------------------------------------------
    # 4. Project organization
    # --------------------------------------------------

    important_folders = [
        "src/",
        "app/",
        "components/",
        "backend/",
        "frontend/",
        "api/",
        "utils/",
        "services/",
        "models/",
        "controllers/"
    ]

    organized_folders = [
        folder
        for folder in important_folders
        if any(
            path.startswith(folder)
            for path in file_paths
        )
    ]

    if len(organized_folders) >= 2:
        score += 5

    return min(score, 20)
def get_maintainability_details(repository_files):

    details = []

    if not repository_files:
        details.append({
            "type": "warning",
            "message": "Repository files could not be analyzed."
        })
        return details

    file_paths = [
        item.get("path", "").lower().strip("/")
        for item in repository_files
        if isinstance(item, dict)
    ]

    # --------------------------------------------------
    # README
    # --------------------------------------------------

    if "readme.md" in file_paths:
        details.append({
            "type": "success",
            "message": "README file found."
        })
    else:
        details.append({
            "type": "warning",
            "message": "README file not found."
        })

    # --------------------------------------------------
    # Git ignore
    # --------------------------------------------------

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

    # --------------------------------------------------
    # Documentation
    # --------------------------------------------------

    documentation_files = [
        path
        for path in file_paths
        if path.endswith(".md")
    ]

    if len(documentation_files) >= 2:
        details.append({
            "type": "success",
            "message": (
                f"{len(documentation_files)} documentation files detected."
            )
        })

    elif len(documentation_files) == 1:
        details.append({
            "type": "warning",
            "message": "Only one documentation file detected."
        })

    else:
        details.append({
            "type": "warning",
            "message": "No documentation files detected."
        })

    # --------------------------------------------------
    # Project organization
    # --------------------------------------------------

    important_folders = [
        "src/",
        "app/",
        "components/",
        "backend/",
        "frontend/",
        "api/",
        "utils/",
        "services/",
        "models/",
        "controllers/"
    ]

    organized_folders = [
        folder
        for folder in important_folders
        if any(
            path.startswith(folder)
            for path in file_paths
        )
    ]

    if len(organized_folders) >= 2:
        details.append({
            "type": "success",
            "message": (
                f"{len(organized_folders)} organized project folders detected."
            )
        })

    elif len(organized_folders) == 1:
        details.append({
            "type": "warning",
            "message": "Only one organized project folder detected."
        })

    else:
        details.append({
            "type": "warning",
            "message": "No common project organization folders detected."
        })

    return details