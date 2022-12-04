from setuptools import setup, packages

with open('requirements.txt') as file:
    important = file.read().splitlines()
setup( 
    name = "snowflake",
    author = "Dhrutiv Jasmin Bhavsar",
    version = "0.0.1",
    author_email = "bhavsardhrutiv@gmail.com",
    url = "https://github.com/DHRVIR/Winter_is_coming.git",
    packages = packages(),
    install_requires = important,
)