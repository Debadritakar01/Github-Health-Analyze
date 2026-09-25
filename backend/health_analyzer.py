
def calculate_documentation_score(repository, readme_content=None):
    score = 0

    # Repository description
    if repository.get("description"):
        score += 5

    # README
    if readme_content:
        score += 10

        readme_lower = readme_content.lower()

        # Check for useful README sections
        useful_sections = [
            "installation",
            "usage",
            "features",
            "technologies",
            "contributing",
        ]

        section_count = sum(
            1 for section in useful_sections
            if section in readme_lower
        )

        score += min(section_count, 5)

    return min(score, 20)

