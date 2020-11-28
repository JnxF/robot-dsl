import codecs
import os

from setuptools import find_packages, setup

PACKAGE_NAME = "robot"
VERSION = "1.0.0"
AUTHOR = "Francisco Martínez Lasaca"
AUTHOR_EMAIL = "frml@itu.dk"
DESCRIPTION = "The Robot language for definig robot behaviour"
KEYWORDS = "textX DSL python domain specific languages robot behaviour"
LICENSE = "MIT"
URL = "www.google.es"

setup(
    name=PACKAGE_NAME,
    version=VERSION,
    description=DESCRIPTION,
    url=URL,
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    keywords=KEYWORDS,
    license=LICENSE,
    packages=find_packages(),
    include_package_data=True,
    package_data={"": ["*.tx"]},
    install_requires=["textx_ls_core"],
    entry_points={"textx_languages": ["robot = tx_robot:robot"]},
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "Intended Audience :: Information Technology",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
)
