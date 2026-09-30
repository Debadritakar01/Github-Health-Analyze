import json


# ============================================================
# DOCUMENTATION ANALYSIS
# ============================================================

def calculate_documentation_score(repository_info, readme_content):

    score = 0

    if not repository_info:
        return score

    # README exists
    if readme_content:
        score += 5

        # Meaningful README content
        if len(readme_content.strip()) >= 200:
            score += 5

    # Repository description
    if repository_info.get("description"):
        score += 3

    # Programming language
    if repository_info.get("language"):
        score += 2

    # README section analysis
    if readme_content:

        readme_lower = readme_content.lower()

        # Installation / Setup
        installation_keywords = [
            "installation",
            "install",
            "setup",
            "getting started"
        ]

        if any(
            keyword in readme_lower
            for keyword in installation_keywords
        ):
            score += 2

        # Usage
        usage_keywords = [
            "usage",
            "how to use",
            "example",
            "run the project"
        ]

        if any(
            keyword in readme_lower
            for keyword in usage_keywords
        ):
            score += 2

        # Features / Project information
        feature_keywords = [
            "features",
            "feature",
            "project",
            "about"
        ]

        if any(
            keyword in readme_lower
            for keyword in feature_keywords
        ):
            score += 1

    return min(score, 20)


def get_documentation_details(repository_info, readme_content):

    details = []

    # README check
    if readme_content:

        details.append({
            "type": "success",
            "message": "README file found."
        })

        # README length
        if len(readme_content.strip()) >= 200:

            details.append({
                "type": "success",
                "message": "README contains meaningful documentation."
            })

        else:

            details.append({
                "type": "warning",
                "message": "README content is very short."
            })

    else:

        details.append({
            "type": "warning",
            "message": "README file not found."
        })

    # Repository description
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

    # Programming language
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

    # README section analysis
    if readme_content:

        readme_lower = readme_content.lower()

        # Installation / Setup
        installation_keywords = [
            "installation",
            "install",
            "setup",
            "getting started"
        ]

        if any(
            keyword in readme_lower
            for keyword in installation_keywords
        ):

            details.append({
                "type": "success",
                "message": "Installation or setup instructions found."
            })

        else:

            details.append({
                "type": "warning",
                "message": "Installation or setup instructions not found."
            })

        # Usage
        usage_keywords = [
            "usage",
            "how to use",
            "example",
            "run the project"
        ]

        if any(
            keyword in readme_lower
            for keyword in usage_keywords
        ):

            details.append({
                "type": "success",
                "message": "Usage information found."
            })

        else:

            details.append({
                "type": "warning",
                "message": "Usage information not found."
            })

        # Features / Project information
        feature_keywords = [
            "features",
            "feature",
            "project",
            "about"
        ]

        if any(
            keyword in readme_lower
            for keyword in feature_keywords
        ):

            details.append({
                "type": "success",
                "message": "Project or feature information found."
            })

        else:

            details.append({
                "type": "warning",
                "message": "Project feature information not found."
            })

    return details


# ============================================================
# PACKAGE.JSON TESTING DETECTION
# ============================================================

def detect_testing_framework_from_package(package_content):

    if not package_content:
        return []

    try:
        package_data = json.loads(package_content)

    except json.JSONDecodeError:
        return []

    dependencies = package_data.get("dependencies", {})
    dev_dependencies = package_data.get("devDependencies", {})

    all_dependencies = {
        **dependencies,
        **dev_dependencies
    }

    testing_frameworks = [
        "jest",
        "vitest",
        "mocha",
        "cypress",
        "playwright"
    ]

    detected_frameworks = []

    for framework in testing_frameworks:

        if framework in all_dependencies:
            detected_frameworks.append(framework)

    return detected_frameworks


def detect_test_script_from_package(package_content):

    if not package_content:
        return False

    try:
        package_data = json.loads(package_content)

    except json.JSONDecodeError:
        return False

    scripts = package_data.get("scripts", {})

    test_script = scripts.get("test")

    if not test_script:
        return False

    return True
def detect_python_testing_framework(repository_files):

    if not repository_files:
        return []

    file_paths = [
        item.get("path", "").lower().strip("/")
        for item in repository_files
        if isinstance(item, dict)
    ]

    detected_frameworks = []

    # pytest configuration
    if any(
        path.split("/")[-1] in ["pytest.ini", "tox.ini"]
        for path in file_paths
    ):
        detected_frameworks.append("pytest")

    # pytest configuration through conftest.py
    if any(
        path.split("/")[-1] == "conftest.py"
        for path in file_paths
    ):
        if "pytest" not in detected_frameworks:
            detected_frameworks.append("pytest")

    return detected_frameworks

# ============================================================
# TESTING ANALYSIS
# ============================================================

def calculate_testing_score(repository_files, package_content=None):

    score = 0

    if not repository_files:
        return score

    file_paths = [
        item.get("path", "").lower().strip("/")
        for item in repository_files
        if isinstance(item, dict)
    ]

    file_paths = [
        path
        for path in file_paths
        if path
    ]

    # --------------------------------
    # 1. Test files or test folders
    # --------------------------------

    test_indicators = [
        "test",
        "tests",
        "__tests__",
        "spec",
        "specs"
    ]

    test_files = []

    for path in file_paths:

        path_parts = path.split("/")

        # Check for test directories anywhere
        has_test_directory = any(
            folder in path_parts
            for folder in test_indicators
        )

        # Check common test file naming conventions
        has_test_extension = (
            path.endswith(".test.js")
            or path.endswith(".test.jsx")
            or path.endswith(".test.ts")
            or path.endswith(".test.tsx")
            or path.endswith(".spec.js")
            or path.endswith(".spec.jsx")
            or path.endswith(".spec.ts")
            or path.endswith(".spec.tsx")
            or path.endswith("_test.py")
            or path.split("/")[-1].startswith("test_")
        )

        if has_test_directory or has_test_extension:
            test_files.append(path)

    # Multiple test files
    if len(test_files) >= 3:
        score += 4

    # --------------------------------
    # 2. Testing frameworks/config
    # --------------------------------

    framework_files = [
        "jest.config.js",
        "jest.config.cjs",
        "jest.config.json",
        "vitest.config.js",
        "vitest.config.ts",
        "pytest.ini",
        "tox.ini",
        ".mocharc.json",
        ".mocharc.js",
        "karma.conf.js"
    ]

    framework_config_detected = any(
        path.split("/")[-1] in framework_files
        for path in file_paths
    )

    detected_frameworks = detect_testing_framework_from_package(
        package_content
    )
    python_frameworks = detect_python_testing_framework(
    repository_files
   )

    detected_frameworks = list(
        dict.fromkeys(
            detected_frameworks + python_frameworks
        )
    )
    framework_detected = (
        framework_config_detected
        or bool(detected_frameworks)
    )

    if framework_detected:
        score += 4

    # --------------------------------
    # 3. Test script
    # --------------------------------

    test_script_detected = detect_test_script_from_package(
        package_content
    )

    if test_script_detected:
        score += 2

    # --------------------------------
    # 4. Python testing configuration
    # --------------------------------

    python_testing_files = [
        "pytest.ini",
        "tox.ini",
        "conftest.py"
    ]

    python_testing_detected = any(
        path.split("/")[-1] in python_testing_files
        for path in file_paths
    )

    if python_testing_detected and not framework_detected:
        score += 3

    # --------------------------------
    # Maximum testing score
    # --------------------------------

    return min(score, 20)


def get_testing_details(repository_files, package_content=None):

    details = []

    if not repository_files:

        details.append({
            "type": "warning",
            "message": "Repository files could not be analyzed for testing."
        })

        return details

    file_paths = [
        item.get("path", "").lower().strip("/")
        for item in repository_files
        if isinstance(item, dict)
    ]

    file_paths = [
        path
        for path in file_paths
        if path
    ]

    # --------------------------------
    # 1. Test files
    # --------------------------------

    test_indicators = [
        "test",
        "tests",
        "__tests__",
        "spec",
        "specs"
    ]

    test_files = []

    for path in file_paths:

        path_parts = path.split("/")

        has_test_directory = any(
            folder in path_parts
            for folder in test_indicators
        )

        has_test_extension = (
            path.endswith(".test.js")
            or path.endswith(".test.jsx")
            or path.endswith(".test.ts")
            or path.endswith(".test.tsx")
            or path.endswith(".spec.js")
            or path.endswith(".spec.jsx")
            or path.endswith(".spec.ts")
            or path.endswith(".spec.tsx")
            or path.endswith("_test.py")
            or path.split("/")[-1].startswith("test_")
        )

        if has_test_directory or has_test_extension:
            test_files.append(path)

    if test_files:

        details.append({
            "type": "success",
            "message": f"Testing files found ({len(test_files)} detected)."
        })

    else:

        details.append({
            "type": "warning",
            "message": "No test files or test directories found."
        })

    # --------------------------------
    # 2. Testing framework
    # --------------------------------

    framework_files = [
        "jest.config.js",
        "jest.config.cjs",
        "jest.config.json",
        "vitest.config.js",
        "vitest.config.ts",
        "pytest.ini",
        "tox.ini",
        ".mocharc.json",
        ".mocharc.js",
        "karma.conf.js"
    ]

    package_frameworks = detect_testing_framework_from_package(
        package_content
    )

    config_frameworks = [
        path.split("/")[-1]
        for path in file_paths
        if path.split("/")[-1] in framework_files
    ]

    if package_frameworks:

        details.append({
            "type": "success",
            "message": (
                "Testing framework detected from package.json: "
                + ", ".join(package_frameworks)
            )
        })

    if config_frameworks:

        details.append({
            "type": "success",
            "message": (
                "Testing framework configuration detected: "
                + ", ".join(config_frameworks)
            )
        })

    if not package_frameworks and not config_frameworks:

        details.append({
            "type": "warning",
            "message": "No testing framework configuration detected."
        })

    # --------------------------------
    # 3. Multiple test files
    # --------------------------------

    if len(test_files) >= 3:

        details.append({
            "type": "success",
            "message": "Multiple test files detected."
        })

    elif len(test_files) > 0:

        details.append({
            "type": "warning",
            "message": "Only a small number of test files were detected."
        })

    # --------------------------------
    # 4. Testing dependencies
    # --------------------------------

    dependency_files = [
        "package.json",
        "requirements.txt",
        "pyproject.toml",
        "pipfile"
    ]

    dependency_exists = any(
        path in dependency_files
        for path in file_paths
    )

    if package_frameworks:

        details.append({
            "type": "success",
            "message": (
                "Testing dependencies detected in package.json: "
                + ", ".join(package_frameworks)
            )
        })

    elif dependency_exists:

        details.append({
            "type": "warning",
            "message": (
                "Dependency file found, but no recognized "
                "testing framework detected."
            )
        })

    else:

        details.append({
            "type": "warning",
            "message": "No clear testing dependency indicators detected."
        })

    # --------------------------------
    # 5. Test script
    # --------------------------------

    test_script_detected = detect_test_script_from_package(
        package_content
    )

    if test_script_detected:

        details.append({
            "type": "success",
            "message": "Test script detected in package.json."
        })

    else:

        details.append({
            "type": "warning",
            "message": "No test script detected in package.json."
        })

    return details


# ============================================================
# CODE STRUCTURE ANALYSIS
# ============================================================
def get_source_files(file_paths):

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

    excluded_config_files = {
        "vite.config.js",
        "vite.config.ts",
        "webpack.config.js",
        "webpack.config.ts",
        "babel.config.js",
        "babel.config.cjs",
        "jest.config.js",
        "jest.config.cjs",
        "vitest.config.js",
        "vitest.config.ts",
        "karma.conf.js"
    }

    source_files = []

    for path in file_paths:

        file_name = path.split("/")[-1]

        # Skip configuration files
        if file_name in excluded_config_files:
            continue

        # Skip test directories
        path_parts = path.split("/")

        if any(
            folder in ["test", "tests", "__tests__", "spec", "specs"]
            for folder in path_parts
        ):
            continue

        # Skip common test naming conventions
        if (
            ".test." in file_name
            or ".spec." in file_name
            or file_name.startswith("test_")
            or file_name.endswith("_test.py")
        ):
            continue

        if path.endswith(source_extensions):
            source_files.append(path)

    return source_files

def calculate_code_structure_score(repository_files):

    score = 0

    if not repository_files:
        return score

    file_paths = [
        item.get("path", "").lower().strip("/")
        for item in repository_files
        if isinstance(item, dict)
    ]

    file_paths = [
        path
        for path in file_paths
        if path
    ]

    # --------------------------------
    # 1. Organized project folders
    # --------------------------------

    important_folder_names = [
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

    organized_folders = []

    for folder in important_folder_names:

        folder_detected = any(
            folder in path.split("/")
            for path in file_paths
        )

        if folder_detected:
            organized_folders.append(folder)

    folder_count = len(organized_folders)

    if folder_count >= 5:
        score += 7

    elif folder_count >= 3:
        score += 5

    elif folder_count >= 1:
        score += 3

    # --------------------------------
    # 2. Source code files
    # --------------------------------

    source_files = get_source_files(file_paths)

    source_count = len(source_files)

    if source_count >= 15:
        score += 5

    elif source_count >= 8:
        score += 4

    elif source_count >= 3:
        score += 2

    # --------------------------------
    # 3. Configuration files
    # --------------------------------

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

    # --------------------------------
    # 4. Nested directory structure
    # --------------------------------

    nested_files = [
        path
        for path in file_paths
        if "/" in path
    ]

    if len(nested_files) >= 5:
        score += 4

    return min(score, 20)


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

    file_paths = [
        path
        for path in file_paths
        if path
    ]

    # --------------------------------
    # 1. Organized project folders
    # --------------------------------

    important_folder_names = [
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

    organized_folders = []

    for folder in important_folder_names:

        folder_detected = any(
            folder in path.split("/")
            for path in file_paths
        )

        if folder_detected:
            organized_folders.append(folder)

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

    # --------------------------------
    # 2. Source code files
    # --------------------------------

    source_files = get_source_files(file_paths)

    details.append({
        "type": "success" if source_files else "warning",
        "message": f"{len(source_files)} source code file(s) detected."
    })

    # --------------------------------
    # 3. Configuration files
    # --------------------------------

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

    # --------------------------------
    # 4. Nested directory structure
    # --------------------------------

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


# ============================================================
# SECURITY ANALYSIS
# ============================================================

def calculate_security_score(repository_files):

    score = 0

    if not repository_files:
        return score

    file_paths = [
        item.get("path", "").lower().strip("/")
        for item in repository_files
        if isinstance(item, dict)
    ]

    file_paths = [
        path
        for path in file_paths
        if path
    ]

    # --------------------------------
    # 6. Security automation
    # --------------------------------

    security_automation_files = [
        ".github/workflows/security-scan.yml",
        ".github/workflows/security-scan.yaml",
        ".github/workflows/dependency-review.yml",
        ".github/workflows/dependency-review.yaml"
    ]

    security_automation_detected = any(
        path in security_automation_files
        for path in file_paths
    )

    if security_automation_detected:
        score += 2

    # --------------------------------
    # 1. Check .gitignore
    # --------------------------------

    if ".gitignore" in file_paths:
        score += 4

    # --------------------------------
    # 2. Check environment template
    # --------------------------------

    environment_files = [
        ".env.example",
        ".env.sample",
        ".env.template"
    ]

    if any(
        path in environment_files
        for path in file_paths
    ):
        score += 3

    # --------------------------------
    # 3. Check security documentation
    # --------------------------------

    security_files = [
        "security.md",
        "security.txt",
        "security/security.md",
        "docs/security.md"
    ]

    if any(
        path in security_files
        for path in file_paths
    ):
        score += 3

    # --------------------------------
    # 4. Check dependency/configuration files
    # --------------------------------

    dependency_files = [
        "package.json",
        "package-lock.json",
        "yarn.lock",
        "pnpm-lock.yaml",
        "requirements.txt",
        "pipfile",
        "poetry.lock",
        "pyproject.toml",
        "pom.xml",
        "build.gradle"
    ]

    detected_dependencies = [
        path
        for path in file_paths
        if path in dependency_files
    ]

    if detected_dependencies:
        score += 3

    # --------------------------------
    # 5. Security configuration files
    # --------------------------------

    security_config_files = [
        ".github/dependabot.yml",
        ".github/dependabot.yaml",
        ".github/workflows/security.yml",
        ".github/workflows/codeql.yml",
        ".github/workflows/codeql.yaml",
        "codeql-config.yml",
        "codeql-config.yaml"
    ]

    detected_security_configs = [
        path
        for path in file_paths
        if path in security_config_files
    ]

    if detected_security_configs:
        score += 3

    # --------------------------------
    # 7. Check suspicious sensitive files
    # --------------------------------

    sensitive_file_names = [
        ".env",
        ".env.local",
        ".env.production",
        ".env.development",
        "credentials.json",
        "credentials.txt",
        "secrets.json",
        "secret.json",
        "private.key",
        "private.pem",
        "id_rsa"
    ]

    sensitive_files = [
        path
        for path in file_paths
        if (
            path in sensitive_file_names
            or path.endswith(".pem")
            or path.endswith(".key")
        )
    ]

    # No sensitive files should not automatically give
# a large security score.
# Only give a small positive point when none are detected.

    if not sensitive_files:
        score += 2

    return min(score, 20)


def get_security_details(repository_files):

    details = []

    if not repository_files:

        details.append({
            "type": "warning",
            "message": "Repository files could not be analyzed for security."
        })

        return details

    file_paths = [
        item.get("path", "").lower().strip("/")
        for item in repository_files
        if isinstance(item, dict)
    ]

    file_paths = [
        path
        for path in file_paths
        if path
    ]

    # --------------------------------
    # 1. .gitignore
    # --------------------------------

    if ".gitignore" in file_paths:

        details.append({
            "type": "success",
            "message": ".gitignore file detected."
        })

    else:

        details.append({
            "type": "warning",
            "message": ".gitignore file is missing."
        })

    # --------------------------------
    # 2. Environment template
    # --------------------------------

    environment_files = [
        ".env.example",
        ".env.sample",
        ".env.template"
    ]

    detected_environment_files = [
        path
        for path in file_paths
        if path in environment_files
    ]

    if detected_environment_files:

        details.append({
            "type": "success",
            "message": "Environment template detected."
        })

    else:

        details.append({
            "type": "warning",
            "message": "No environment template file detected."
        })

    # --------------------------------
    # 3. Security documentation
    # --------------------------------

    security_files = [
        "security.md",
        "security.txt",
        "security/security.md",
        "docs/security.md"
    ]

    detected_security_files = [
        path
        for path in file_paths
        if path in security_files
    ]

    if detected_security_files:

        details.append({
            "type": "success",
            "message": "Security documentation detected."
        })

    else:

        details.append({
            "type": "warning",
            "message": "Security documentation not found."
        })

    # --------------------------------
    # 4. Dependency files
    # --------------------------------

    dependency_files = [
        "package.json",
        "package-lock.json",
        "yarn.lock",
        "pnpm-lock.yaml",
        "requirements.txt",
        "pipfile",
        "poetry.lock",
        "pyproject.toml",
        "pom.xml",
        "build.gradle"
    ]

    detected_dependencies = [
        path
        for path in file_paths
        if path in dependency_files
    ]

    if detected_dependencies:

        details.append({
            "type": "success",
            "message": (
                "Dependency/configuration files detected: "
                + ", ".join(detected_dependencies)
            )
        })

    else:

        details.append({
            "type": "warning",
            "message": "No common dependency files detected."
        })
        # --------------------------------
    # 5. Security configuration
    # --------------------------------

    security_config_files = [
        ".github/dependabot.yml",
        ".github/dependabot.yaml",
        ".github/workflows/security.yml",
        ".github/workflows/security.yaml",
        ".github/workflows/codeql.yml",
        ".github/workflows/codeql.yaml",
        "codeql-config.yml",
        "codeql-config.yaml"
    ]

    detected_security_configs = [
        path
        for path in file_paths
        if path in security_config_files
    ]

    if detected_security_configs:

        details.append({
            "type": "success",
            "message": (
                "Security configuration detected: "
                + ", ".join(detected_security_configs)
            )
        })

    else:

        details.append({
            "type": "warning",
            "message": "No security configuration files detected."
        })

    # --------------------------------
    # 6. Security automation
    # --------------------------------

    security_automation_files = [
        ".github/workflows/security-scan.yml",
        ".github/workflows/security-scan.yaml",
        ".github/workflows/dependency-review.yml",
        ".github/workflows/dependency-review.yaml"
    ]

    detected_security_automation = [
        path
        for path in file_paths
        if path in security_automation_files
    ]

    if detected_security_automation:

        details.append({
            "type": "success",
            "message": (
                "Security automation detected: "
                + ", ".join(detected_security_automation)
            )
        })

    else:

        details.append({
            "type": "warning",
            "message": "No security automation workflow detected."
        })
    # --------------------------------
    # 7. Sensitive files
    # --------------------------------

    sensitive_file_names = [
        ".env",
        ".env.local",
        ".env.production",
        ".env.development",
        ".env.test",
        "credentials.json",
        "credentials.txt",
        "secrets.json",
        "secret.json",
        "private.key",
        "private.pem",
        "id_rsa",
        "id_rsa.pem",
        "server.key",
        "server.pem"
    ]

    sensitive_files = [
        path
        for path in file_paths
        if (
            path in sensitive_file_names
            or path.endswith(".pem")
            or path.endswith(".key")
        )
    ]

    if sensitive_files:

        details.append({
            "type": "warning",
            "message": (
                "Potentially sensitive files detected: "
                + ", ".join(sensitive_files)
            )
        })

    else:

        details.append({
            "type": "success",
            "message": "No obvious sensitive files detected."
        })

    return details


# ============================================================
# MAINTAINABILITY ANALYSIS
# ============================================================

def calculate_maintainability_score(repository_files):

    score = 0

    if not repository_files:
        return score

    file_paths = [
        item.get("path", "").lower().strip("/")
        for item in repository_files
        if isinstance(item, dict)
    ]

    file_paths = [
        path
        for path in file_paths
        if path
    ]

    # --------------------------------
    # 1. README / Documentation
    # --------------------------------

    documentation_files = [
        "readme.md",
        "readme.txt",
        "readme"
    ]

    if any(
        path in documentation_files
        for path in file_paths
    ):
        score += 4

    # --------------------------------
    # 2. Organized source structure
    # --------------------------------

    important_folder_names = [
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

    organized_folders = []

    for folder in important_folder_names:

        folder_detected = any(
            folder in path.split("/")
            for path in file_paths
        )

        if folder_detected:
            organized_folders.append(folder)

    if len(organized_folders) >= 3:
        score += 4

    elif len(organized_folders) >= 1:
        score += 2

    # --------------------------------
    # 3. Source-file organization
    # --------------------------------

    source_files = get_source_files(file_paths)

    source_count = len(source_files)

    if 3 <= source_count <= 100:
        score += 4

    elif source_count > 0:
        score += 2

    # --------------------------------
    # 4. Dependency / configuration management
    # --------------------------------

    configuration_files = [
        "package.json",
        "package-lock.json",
        "yarn.lock",
        "pnpm-lock.yaml",
        "requirements.txt",
        "pipfile",
        "pyproject.toml",
        "poetry.lock",
        "pom.xml",
        "build.gradle",
        "tsconfig.json"
    ]

    detected_configs = [
        path
        for path in file_paths
        if path in configuration_files
    ]

    if detected_configs:
        score += 4

    # --------------------------------
    # 5. Temporary / duplicate-looking files
    # --------------------------------

    temporary_indicators = [
        ".tmp",
        ".temp",
        ".bak",
        ".old",
        ".backup",
        "~"
    ]

    temporary_files = [
        path
        for path in file_paths
        if any(
            path.endswith(indicator)
            for indicator in temporary_indicators
        )
    ]

    if not temporary_files:
        score += 4

    return min(score, 20)


def get_maintainability_details(repository_files):

    details = []

    if not repository_files:

        details.append({
            "type": "warning",
            "message": "Repository files could not be analyzed for maintainability."
        })

        return details

    file_paths = [
        item.get("path", "").lower().strip("/")
        for item in repository_files
        if isinstance(item, dict)
    ]

    file_paths = [
        path
        for path in file_paths
        if path
    ]

    # --------------------------------
    # 1. README / Documentation
    # --------------------------------

    documentation_files = [
        "readme.md",
        "readme.txt",
        "readme"
    ]

    if any(
        path in documentation_files
        for path in file_paths
    ):

        details.append({
            "type": "success",
            "message": "README/documentation file detected."
        })

    else:

        details.append({
            "type": "warning",
            "message": "README/documentation file not detected."
        })

    # --------------------------------
    # 2. Organized source structure
    # --------------------------------

    important_folder_names = [
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

    organized_folders = []

    for folder in important_folder_names:

        folder_detected = any(
            folder in path.split("/")
            for path in file_paths
        )

        if folder_detected:
            organized_folders.append(folder)

    if len(organized_folders) >= 3:

        details.append({
            "type": "success",
            "message": (
                "Multiple organized project folders detected: "
                + ", ".join(organized_folders)
            )
        })

    elif organized_folders:

        details.append({
            "type": "warning",
            "message": (
                "Some project organization detected: "
                + ", ".join(organized_folders)
            )
        })

    else:

        details.append({
            "type": "warning",
            "message": "No common organized project folders detected."
        })

    # --------------------------------
    # 3. Source-file organization
    # --------------------------------

    source_files = get_source_files(file_paths)

    source_count = len(source_files)

    if 3 <= source_count <= 100:

        details.append({
            "type": "success",
            "message": (
                f"{source_count} source code files detected, "
                "indicating a manageable project structure."
            )
        })

    elif source_count > 0:

        details.append({
            "type": "warning",
            "message": (
                f"{source_count} source code files detected."
            )
        })

    else:

        details.append({
            "type": "warning",
            "message": "No source code files detected."
        })

    # --------------------------------
    # 4. Configuration / dependency management
    # --------------------------------

    configuration_files = [
        "package.json",
        "package-lock.json",
        "yarn.lock",
        "pnpm-lock.yaml",
        "pipfile",
        "requirements.txt",
        "pyproject.toml",
        "poetry.lock",
        "pom.xml",
        "build.gradle",
        "tsconfig.json"
    ]

    detected_configs = [
        path
        for path in file_paths
        if path in configuration_files
    ]

    if detected_configs:

        details.append({
            "type": "success",
            "message": (
                "Dependency/configuration files detected: "
                + ", ".join(detected_configs)
            )
        })

    else:

        details.append({
            "type": "warning",
            "message": "No common dependency/configuration files detected."
        })

    # --------------------------------
    # 5. Temporary / duplicate-looking files
    # --------------------------------

    temporary_indicators = [
        ".tmp",
        ".temp",
        ".bak",
        ".old",
        ".backup",
        "~"
    ]

    temporary_files = [
        path
        for path in file_paths
        if any(
            path.endswith(indicator)
            for indicator in temporary_indicators
        )
    ]

    if temporary_files:

        details.append({
            "type": "warning",
            "message": (
                "Temporary or backup-looking files detected: "
                + ", ".join(temporary_files)
            )
        })

    else:

        details.append({
            "type": "success",
            "message": "No obvious temporary or backup files detected."
        })

    return details
# ============================================================
# RECOMMENDATIONS
# ============================================================

def generate_recommendations(
    documentation_details,
    testing_details,
    code_structure_details,
    security_details,
    maintainability_details
):

    recommendations = []


    # ========================================================
    # DOCUMENTATION RECOMMENDATIONS
    # ========================================================

    for detail in documentation_details or []:

        if detail.get("type") != "warning":
            continue

        message = detail.get("message", "")
        message_lower = message.lower()

        recommendation = (
            "Improve the repository documentation "
            "by adding the missing information."
        )

        if "readme" in message_lower:
            recommendation = (
                "Add or improve the README.md file with "
                "clear project information, setup instructions, "
                "usage instructions, and important features."
            )

        elif "description" in message_lower:
            recommendation = (
                "Add a clear repository description explaining "
                "the purpose and functionality of the project."
            )

        elif "language" in message_lower:
            recommendation = (
                "Make sure the repository contains recognizable "
                "source files so the primary programming language "
                "can be identified."
            )

        elif "installation" in message_lower or "setup" in message_lower:
            recommendation = (
                "Add a Setup or Installation section to the README "
                "with the steps required to run the project locally."
            )

        elif "usage" in message_lower:
            recommendation = (
                "Add a Usage section explaining how users or "
                "developers can use the application."
            )

        elif "feature" in message_lower:
            recommendation = (
                "Document the main features and capabilities "
                "of the project in the README."
            )

        recommendations.append({
            "category": "Documentation",
            "priority": "Medium",
            "message": message,
            "recommendation": recommendation
        })


    # ========================================================
    # TESTING RECOMMENDATIONS
    # ========================================================

    for detail in testing_details or []:

        if detail.get("type") != "warning":
            continue

        message = detail.get("message", "")
        message_lower = message.lower()

        recommendation = (
            "Add automated tests and configure a testing "
            "framework for the project."
        )

        if "test file" in message_lower or "test folder" in message_lower:
            recommendation = (
                "Create a dedicated tests or __tests__ folder "
                "and add unit or integration test files for "
                "important project functionality."
            )

        elif "configuration" in message_lower or "config" in message_lower:
            recommendation = (
                "Add a testing configuration such as Jest, "
                "Vitest, Pytest, or another framework appropriate "
                "for the project's technology stack."
            )

        elif "dependency" in message_lower:
            recommendation = (
                "Add the required testing dependencies to the "
                "project dependency configuration."
            )

        elif "script" in message_lower:
            recommendation = (
                "Add a convenient test script to package.json "
                "or the project's build configuration so tests "
                "can be executed easily."
            )

        recommendations.append({
            "category": "Testing",
            "priority": "High",
            "message": message,
            "recommendation": recommendation
        })


    # ========================================================
    # CODE STRUCTURE RECOMMENDATIONS
    # ========================================================

    for detail in code_structure_details or []:

        if detail.get("type") != "warning":
            continue

        message = detail.get("message", "")
        message_lower = message.lower()

        recommendation = (
            "Organize source files into clear folders "
            "and keep related functionality together."
        )

        if "folder" in message_lower:
            recommendation = (
                "Create clear directories such as components, "
                "services, utilities, pages, or modules to "
                "organize related files."
            )

        elif "source" in message_lower:
            recommendation = (
                "Maintain a clear source-code structure and "
                "separate application logic into appropriate "
                "modules or components."
            )

        elif "config" in message_lower:
            recommendation = (
                "Keep project configuration files organized "
                "and clearly separated from application source code."
            )

        elif "nested" in message_lower:
            recommendation = (
                "Use meaningful nested folders where necessary "
                "to group related functionality without creating "
                "an unnecessarily deep directory structure."
            )

        recommendations.append({
            "category": "Code Structure",
            "priority": "Medium",
            "message": message,
            "recommendation": recommendation
        })


    # ========================================================
    # SECURITY RECOMMENDATIONS
    # ========================================================

    for detail in security_details or []:

        if detail.get("type") != "warning":
            continue

        message = detail.get("message", "")
        message_lower = message.lower()

        recommendation = (
            "Review the repository security configuration "
            "and make sure sensitive files and credentials "
            "are protected."
        )

        if "gitignore" in message_lower:
            recommendation = (
                "Add a .gitignore file and exclude sensitive "
                "files such as .env files, credentials, virtual "
                "environments, build files, and local configuration."
            )

        elif "env" in message_lower:
            recommendation = (
                "Add an environment-variable template such as "
                ".env.example and keep real credentials outside "
                "the repository."
            )

        elif "security" in message_lower:
            recommendation = (
                "Add security documentation describing how "
                "credentials, authentication, sensitive data, "
                "and security-related configuration are handled."
            )

        elif "dependency" in message_lower:
            recommendation = (
                "Maintain a dependency file such as "
                "requirements.txt or package.json and keep "
                "dependencies updated."
            )

        elif "sensitive" in message_lower:
            recommendation = (
                "Remove sensitive or credential-like files from "
                "the repository and add appropriate patterns to "
                ".gitignore."
            )

        recommendations.append({
            "category": "Security",
            "priority": "High",
            "message": message,
            "recommendation": recommendation
        })


    # ========================================================
    # MAINTAINABILITY RECOMMENDATIONS
    # ========================================================

    for detail in maintainability_details or []:

        if detail.get("type") != "warning":
            continue

        message = detail.get("message", "")
        message_lower = message.lower()

        recommendation = (
            "Improve the project structure, documentation, "
            "and configuration to make future maintenance easier."
        )

        if "readme" in message_lower or "documentation" in message_lower:
            recommendation = (
                "Maintain clear project documentation so future "
                "developers can understand the purpose, setup, "
                "usage, and structure of the project."
            )

        elif "folder" in message_lower or "organized" in message_lower:
            recommendation = (
                "Organize related source files into meaningful "
                "folders and keep the project structure consistent."
            )

        elif "source" in message_lower:
            recommendation = (
                "Keep source files modular and avoid placing too "
                "much functionality into a single file."
            )

        elif "config" in message_lower:
            recommendation = (
                "Keep configuration files clearly organized and "
                "use standard project configuration practices."
            )

        elif (
            "temporary" in message_lower
            or "backup" in message_lower
            or "temp" in message_lower
        ):
            recommendation = (
                "Remove temporary, backup, generated, or unnecessary "
                "files from the repository to keep the codebase clean."
            )

        recommendations.append({
            "category": "Maintainability",
            "priority": "Medium",
            "message": message,
            "recommendation": recommendation
        })


    return recommendations