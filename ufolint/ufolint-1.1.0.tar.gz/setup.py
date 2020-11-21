import io
import os
import re
import sys
from setuptools import setup, find_packages

REQUIRES_PYTHON = ">=3.6.0"

# Optional packages
EXTRAS_REQUIRES = {
    # for developer installs
    "dev": [
        "wheel",
        "setuptools",
        "twine",
        "coverage",
        "pytest",
        "tox",
        "flake8",
        "pytype",
    ]
}


def version_read():
    settings_file = open(
        os.path.join(os.path.dirname(__file__), "lib", "ufolint", "settings.py")
    ).read()
    major_regex = r"""major_version\s*?=\s*?["']{1}(\d+)["']{1}"""
    minor_regex = r"""minor_version\s*?=\s*?["']{1}(\d+)["']{1}"""
    patch_regex = r"""patch_version\s*?=\s*?["']{1}(\d+)["']{1}"""
    major_match = re.search(major_regex, settings_file)
    minor_match = re.search(minor_regex, settings_file)
    patch_match = re.search(patch_regex, settings_file)
    major_version = major_match.group(1)
    minor_version = minor_match.group(1)
    patch_version = patch_match.group(1)
    if len(major_version) == 0:
        major_version = 0
    if len(minor_version) == 0:
        minor_version = 0
    if len(patch_version) == 0:
        patch_version = 0
    return major_version + "." + minor_version + "." + patch_version


# Use repository Markdown README.md for PyPI long description
try:
    with io.open("README.md", encoding="utf-8") as f:
        readme = f.read()
except IOError as readme_e:
    sys.stderr.write(
        "[ERROR] setup.py: Failed to read the README.md file for the long description definition: {}".format(
            str(readme_e)
        )
    )
    raise readme_e

setup(
    name="ufolint",
    version=version_read(),
    description="UFO source file linter",
    long_description=readme,
    long_description_content_type="text/markdown",
    url="https://github.com/source-foundry/ufolint",
    license="MIT license",
    author="Christopher Simpkins",
    author_email="chris@sourcefoundry.org",
    platforms=["any"],
    packages=find_packages("lib"),
    package_dir={"": "lib"},
    install_requires=["commandlines", "fontTools[ufo]>=3.31.0"],
    entry_points={
        "console_scripts": ["ufolint = ufolint.app:main"],
    },
    keywords="",
    include_package_data=True,
    extras_require=EXTRAS_REQUIRES,
    python_requires=REQUIRES_PYTHON,
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Natural Language :: English",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Text Processing :: Fonts",
    ],
)
