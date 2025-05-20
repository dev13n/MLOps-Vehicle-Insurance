from setuptools import setup, find_packages

setup(
    name="src",
    version="0.0.1",
    author="Dev N",
    author_email="devpn02@gmail.com",
    # Automatically discover and include all packages in the directory (excluding those like tests if specified)
    packages=find_packages()
)