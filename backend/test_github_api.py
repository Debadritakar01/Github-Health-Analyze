import asyncio

from github_api import get_file_content
from health_analyzer import (
    detect_testing_framework_from_package,
    detect_test_script_from_package
)
fake_test_package = """
{
    "scripts": {
        "dev": "vite",
        "test": "vitest"
    }
}
"""

has_test_script = detect_test_script_from_package(
    fake_test_package
)

print("Test script detected:")
print(has_test_script)
async def main():

    content = await get_file_content(
        "Debadritakar01",
        "Github-Health-Analyze",
        "package.json"
    )

    frameworks = detect_testing_framework_from_package(content)

    print("Real package.json:")
    print(frameworks)

    # Temporary test
    fake_package = """
    {
        "dependencies": {},
        "devDependencies": {
            "vitest": "^3.0.0"
        }
    }
    """

    fake_frameworks = detect_testing_framework_from_package(
        fake_package
    )

    print("Fake package.json:")
    print(fake_frameworks)


asyncio.run(main())