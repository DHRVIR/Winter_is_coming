from setuptools import setup, find_packages

with open('requirenments.txt') as file:
    required = file.read().splitlines()
print(required)
setup( 
    name = "snowflake",
    author = "Dhrutiv Jasmin Bhavsar",
    version = "0.0.1",
    author_email = "bhavsardhrutiv@gmail.com",
    url = "https://github.com/DHRVIR/Winter_is_coming.git",
    packages = find_packages(),
    install_requires = required
)
print(type(required))