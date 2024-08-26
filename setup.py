import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()


__version__ = "0.0.0"

REPO_NAME = "Recommendation-Assistent"
AUTHOR_USER_NAME = "VladimirKalajcidi"
SRC_REPO = "recommendationAssistant"
AUTHOR_EMAIL = "vovchik2006kalaychidi@gmail.com"


setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A small python package for recommendations",
    long_description=long_description,
    long_description_content="text/markdown",
    url=f"https://gitlab.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://gitlab.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src")
)