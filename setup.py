#!/usr/bin/env python3

import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="configprops",
    version="0.1.1",
    author="Xu Yijun",
    author_email="xuyijun@gmail.com",
    description="'configprops' defines a set of KEYS (sharing prefix) as configuration keys. Allow overriding from environment variables.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/tommyxu/configprops",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
