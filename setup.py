from setuptools import setup, find_packages
import os

with open('requirements.txt') as files:
    important = files.read().splitlines()
setup( 
    name = "snowflake",
    author = "Dhrutiv Jasmin Bhavsar",
    version = "0.0.1",
    url = "https://github.com/DHRVIR/Winter_is_coming.git",
    author_email="bhavsardhrutiv@gmail.com",
    packages = find_packages(),
    install_requires = important
)
