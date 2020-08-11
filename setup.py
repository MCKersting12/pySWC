# -*- coding: utf-8 -*-
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="MCKersting12", # Replace with your own username
    version="0.0.1",
    author="Matthew Kersting",
    author_email="MattKersting2019@gmail.com",
    description="Package used for manipulating swc files",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/MCKersting12/pySWC",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)