from setuptools import setup, find_packages
from os import path

version = "0.0.5"

this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, "README.md"), encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="dataspace",
    packages=find_packages(),
    version=version,
    description="Data wrangling and visualization",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="synw",
    author_email="synwe@yahoo.com",
    url="https://github.com/synw/dataspace",
    download_url="https://github.com/synw/dataspace/releases/tag/" + version,
    keywords=["data_visualization", "data_exploration", "charts"],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.8",
    ],
    install_requires=["pandas", "altair", "holoviews"],
    zip_safe=False,
)
