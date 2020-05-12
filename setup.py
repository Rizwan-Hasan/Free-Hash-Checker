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
    name="hash-checker",
    version="3.0",
    description="A simple and elegant open-source hash checker software.",
    long_description="A simple and elegant open-source hash checker software.",
    url="https://rizwan-hasan.github.io/hash-checker/",
    author="Rizwan Hasan",
    author_email="rizwan.hasan486@gmail.com",
    license="MIT",
    keywords="utility hash hashing md5 sha1 sha224 sha256 sha384 sha512",
    project_urls={
        "Source code": "https://github.com/Rizwan-Hasan/hash-checker",
        "Bug tracker": "https://github.com/Rizwan-Hasan/hash-checker/issues",
    },
    platforms=["Windows", "macOS", "Linux"],
    install_requires=requirements,
    python_requires=">=3.7",
    packages=find_packages(),
    package_data={
        "hashchecker.ui": ["ui"],
    },
    entry_points={
        "console_scripts": ["hash-checker = hashchecker.AppRun:main"],
        "gui_scripts": ["hash-checker = hashchecker.AppRun:main"]
    }
)
