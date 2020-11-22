import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="numbersII",
    version="0.0.4",
    author="ettoredangelo",
    author_email="ettoredangelo@gmail.com",
    description="A small library for the lesson on clustering at NumbersII",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ettoredangelo/numbersII",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)