import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="us-school-data-api",
    version="0.0.1",
    author="Ari Israel",
    author_email="ari@ariisrael.com",
    description="Python wrapper for the Urban Institute School and School Districts API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ariisrael/us-education-data-api",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    keywords=['united states', 'education data', 'urban institute', 'api wrapper', 'schools', 'school districts']
)