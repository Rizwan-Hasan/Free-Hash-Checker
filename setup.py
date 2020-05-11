import os.path
import sys

from setuptools import find_packages, setup


if sys.version_info < (3, 7):
    raise RuntimeError("Free Hash Checker requires Python 3.7 or later")

setupdir = os.path.dirname(__file__)

requirements = []
for line in open(os.path.join(setupdir, "requirements.txt"), encoding="ASCII"):
    if line.strip() and not line.startswith("#"):
        requirements.append(line)

setup(
    name="free-hash-checker",
    version="3.0",
    description="A simple and elegant open-source hash checker software.",
    long_description="A simple and elegant open-source hash checker software.",
    url="https://rizwan-hasan.github.io/Free-Hash-Checker/",
    author="Rizwan Hasan",
    author_email="rizwan.hasan486@gmail.com",
    license="MIT",
    keywords="utility hash",
    project_urls={
        "Source code": "https://github.com/Rizwan-Hasan/Free-Hash-Checker",
        "Bug tracker": "https://github.com/Rizwan-Hasan/Free-Hash-Checker/issues",
    },
    platforms=["Windows", "macOS", "Linux"],
    install_requires=requirements,
    python_requires=">=3.7",
    packages=find_packages(),
    package_data={
        "freeHashChecker.ui": ["ui"],
    },
    entry_points={
        "console_scripts": ["free-hash-checker = freeHashChecker.AppRun:main"],
        "gui_scripts": ["free-hash-checker = freeHashChecker.AppRun:main"]
    },
)
