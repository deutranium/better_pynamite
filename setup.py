from setuptools import setup, find_packages
from pathlib import Path

VERSION = "0.1.4"
DESCRIPTION = "Import and create chaos"


# read the contents of README file
this_directory = Path(__file__).parent
LONG_DESCRIPTION = (this_directory / "README.md").read_text()

setup(
    name="better_pynamite",
    version=VERSION,
    author="Kshitijaa Jaglan",
    author_email="kshitijaa.jaglan@research.iiit.ac.in",
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    long_description_content_type='text/markdown',
    url="https://github.com/deutranium/better_pynamite",
    packages=find_packages(),
    install_requires=[],
    keywords=["python", "chaos"],
    classifiers=[],
    license="Apache License 2.0",
)
