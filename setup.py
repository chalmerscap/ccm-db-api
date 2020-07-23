import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="borsdata-api-utils-maxijohansson", # Replace with your own username
    version="0.0.1",
    author="Max Johansson",
    description="Borsdata api functions",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/maxijohansson/borsdata_api_utils",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)