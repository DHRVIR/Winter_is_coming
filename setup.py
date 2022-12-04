from setuptools import setup, find_packages

with open('requirenments.txt') as f:
    required = f.read().splitlines()
    
setup( 
    name = "snowflake",
    author = "Dhrutiv Jasmin Bhavsar",
    version = "0.0.1",
    packages = find_packages(),
    install_requires = required
)
print(type(required))