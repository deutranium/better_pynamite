from setuptools import setup, find_packages

VERSION = "0.1"
DESCRIPTION = "Import and create chaos"
LONG_DESCRIPTION = "Import pynamite to stop script execution at random"

setup(
    name="better_pynamite",
    version=VERSION,
    author="Kshitijaa Jaglan",
    author_email="kshitijaa.jaglan@research.iiit.ac.in",
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    url="https://github.com/deutranium/better_pynamite",
    packages=find_packages(),
    install_requires=[],
    keywords=["python", "chaos"],
    classifiers=[],
    license="MIT",
)
