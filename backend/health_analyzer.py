
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
# TESTING ANALYSIS
# ============================================================


def calculate_testing_score(repository_files):

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
        "test/",
        "tests/",
        "__tests__/",
        "spec/",
        "specs/"
    ]

    test_files = [
        path
        for path in file_paths
        if (
            any(path.startswith(folder) for folder in test_indicators)
            or path.endswith(".test.js")
            or path.endswith(".test.jsx")
            or path.endswith(".test.ts")
            or path.endswith(".test.tsx")
            or path.endswith(".spec.js")
            or path.endswith(".spec.jsx")
            or path.endswith(".spec.ts")
            or path.endswith(".spec.tsx")
            or path.endswith("_test.py")
            or path.startswith("test_")
        )
    ]

    if test_files:
        score += 5

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
        "pyproject.toml",
        "tox.ini",
        ".mocharc.json",
        ".mocharc.js",
        "karma.conf.js"
    ]

    if any(
        path in framework_files
        for path in file_paths
    ):
        score += 5

    # --------------------------------
    # 3. Multiple test files
    # --------------------------------

    if len(test_files) >= 3:
        score += 4

    # --------------------------------
    # 4. Testing dependencies
    # --------------------------------

    dependency_files = [
        "package.json",
        "requirements.txt",
        "pyproject.toml",
        "pipfile"
    ]

    dependency_file_exists = any(
        path in dependency_files
        for path in file_paths
    )

    testing_dependency_names = [
        "jest",
        "vitest",
        "mocha",
        "chai",
        "pytest",
        "unittest",
        "selenium",
        "cypress",
        "playwright"
    ]

    testing_dependency_files = [
        path
        for path in file_paths
        if any(
            dependency in path
            for dependency in testing_dependency_names
        )
    ]

    if dependency_file_exists and testing_dependency_files:
        score += 3

    # --------------------------------
    # 5. Test scripts/configuration
    # --------------------------------

    script_indicators = [
        "test script",
        "test",
        "testing",
        "npm test"
    ]

    script_files = [
        path
        for path in file_paths
        if any(
            indicator in path
            for indicator in script_indicators
        )
    ]

    if script_files:
        score += 3

    return min(score, 20)


def get_testing_details(repository_files):

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

    test_files = [
        path
        for path in file_paths
        if (
            path.startswith("test/")
            or path.startswith("tests/")
            or path.startswith("__tests__/")
            or path.startswith("spec/")
            or path.startswith("specs/")
            or path.endswith(".test.js")
            or path.endswith(".test.jsx")
            or path.endswith(".test.ts")
            or path.endswith(".test.tsx")
            or path.endswith(".spec.js")
            or path.endswith(".spec.jsx")
            or path.endswith(".spec.ts")
            or path.endswith(".spec.tsx")
            or path.endswith("_test.py")
            or path.startswith("test_")
        )
    ]

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

    detected_frameworks = [
        path
        for path in file_paths
        if path in framework_files
    ]

    if detected_frameworks:

        details.append({
            "type": "success",
            "message": "Testing framework configuration detected."
        })

    else:

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

    testing_dependency_names = [
        "jest",
        "vitest",
        "mocha",
        "chai",
        "pytest",
        "unittest",
        "selenium",
        "cypress",
        "playwright"
    ]

    dependency_exists = any(
        path in dependency_files
        for path in file_paths
    )

    testing_dependency_detected = any(
        any(
            dependency in path
            for dependency in testing_dependency_names
        )
        for path in file_paths
    )

    if dependency_exists and testing_dependency_detected:

        details.append({
            "type": "success",
            "message": "Testing dependency indicators detected."
        })

    else:

        details.append({
            "type": "warning",
            "message": "No clear testing dependency indicators detected."
        })

    # --------------------------------
    # 5. Test scripts/configuration
    # --------------------------------

    test_script_files = [
        path
        for path in file_paths
        if (
            "test" in path
            or "testing" in path
        )
    ]

    if test_script_files:

        details.append({
            "type": "success",
            "message": "Test-related configuration or scripts detected."
        })

    else:

        details.append({
            "type": "warning",
            "message": "No test-related scripts or configuration detected."
        })

    return details


# ============================================================
# CODE STRUCTURE ANALYSIS
# ============================================================

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

    # --------------------------------
    # 2. Source code files
    # --------------------------------

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

    # --------------------------------
    # 2. Source code files
    # --------------------------------

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

    # --------------------------------------------------
    # 1. Check .gitignore
    # --------------------------------------------------

    if ".gitignore" in file_paths:
        score += 4

    # --------------------------------------------------
    # 2. Check environment template
    # --------------------------------------------------

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

    # --------------------------------------------------
    # 3. Check security documentation
    # --------------------------------------------------

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

    # --------------------------------------------------
    # 4. Check dependency/configuration files
    # --------------------------------------------------

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

    # --------------------------------------------------
    # 5. Check for suspicious sensitive files
    # --------------------------------------------------

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

    # Give security points when no obvious sensitive files
    # are detected.
    if not sensitive_files:
        score += 7

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

    # --------------------------------------------------
    # 1. .gitignore
    # --------------------------------------------------

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

    # --------------------------------------------------
    # 2. Environment template
    # --------------------------------------------------

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

    # --------------------------------------------------
    # 3. Security documentation
    # --------------------------------------------------

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

    # --------------------------------------------------
    # 4. Dependency files
    # --------------------------------------------------

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

    # --------------------------------------------------
    # 5. Sensitive files
    # --------------------------------------------------

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

    # --------------------------------------------------
    # 1. README / Documentation
    # --------------------------------------------------

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

    # --------------------------------------------------
    # 2. Organized source structure
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

    if len(organized_folders) >= 3:
        score += 4
    elif len(organized_folders) >= 1:
        score += 2

    # --------------------------------------------------
    # 3. Source-file organization
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

    if 3 <= source_count <= 100:
        score += 4
    elif source_count > 0:
        score += 2

    # --------------------------------------------------
    # 4. Dependency / configuration management
    # --------------------------------------------------

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

    # --------------------------------------------------
    # 5. Temporary / duplicate-looking files
    # --------------------------------------------------

    temporary_indicators = [
        ".tmp",
        ".temp",
        ".bak",
        ".old",
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

    # --------------------------------------------------
    # 1. README / Documentation
    # --------------------------------------------------

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

    # --------------------------------------------------
    # 2. Organized source structure
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

    # --------------------------------------------------
    # 3. Source-file organization
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

    # --------------------------------------------------
    # 4. Configuration / dependency management
    # --------------------------------------------------

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

    # --------------------------------------------------
    # 5. Temporary / duplicate-looking files
    # --------------------------------------------------

    temporary_indicators = [
        ".tmp",
        ".temp",
        ".bak",
        ".old",
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



