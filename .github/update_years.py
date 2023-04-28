import os
from datetime import datetime
from github import Github

START_YEAR = 2011
REPO_NAME = "seancheong/seancheong"
UPDATE_FILE = "README.md"


def update_years():
    current_year = datetime.now().year
    experience = current_year - START_YEAR

    with open(UPDATE_FILE, "r") as readme_file:
        content = readme_file.read()

    new_content = content.replace(
        f"{experience - 1} years of coding experience",
        f"{experience} years of coding experience"
    )

    if content != new_content:
        with open(UPDATE_FILE, "w") as readme_file:
            readme_file.write(new_content)

        github = Github(os.environ["GH_TOKEN"])
        repo = github.get_repo(REPO_NAME)
        repo.update_file(
            path=UPDATE_FILE,
            message=f"Update experience to {experience} years",
            content=new_content,
            sha=repo.get_contents(UPDATE_FILE).sha
        )


if __name__ == "__main__":
    update_years()
