import setuptools
version = '0.0.0'
repo_name = "poetry-generation"
username = "ripesh"
author_email = "ripeshghimire987@gmail.com"
src_repo = 'POETRYGENERATION'
from typing import List
HYPEN_E_DOT  = '-e .'

setuptools.setup(
    name = repo_name,
    version= version,
    author= username,
    author_email= author_email,
    description= "A small python package for NLP APP",
    url=f"https://github.com/{username}/{repo_name}",
    project_urls={
        "Bug Tracker": f"https://github.com/{username}/{repo_name}/issues",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src")
)
