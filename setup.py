from setuptools import setup, find_packages

with open('requirenments.txt') as file:
    imp = file.read().splitlines()
setup( 
    name = "snowflake",
    author = "Dhrutiv Jasmin Bhavsar",
    version = "0.0.1",
    author_email = "bhavsardhrutiv@gmail.com",
    url = "https://github.com/DHRVIR/Winter_is_coming.git",
    packages = find_packages(),
    install_requires = imp
)