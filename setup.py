#!/usr/bin/env python3

from distutils.core import setup

# with open("README.md", "r") as fh:
#     long_description = fh.read()

setup(
    name="configprops",
    version="1.0.0",
    author="Xu Yijun",
    author_email="xuyijun@gmail.com",
    description=
    "'configprops' defines a set of KEYS (sharing prefix) as configuration keys. Allow overriding from environment variables.",
    # long_description=long_description,
    # long_description_content_type="text/markdown",
    url="https://github.com/tommyxu/configprops",
    packages=['configprops'],
    requires=['termcolor'],
    setup_requires=['wheel'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
