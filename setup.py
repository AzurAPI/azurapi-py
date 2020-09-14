from setuptools import setup

# The version number
version = "1.1.2"

# README
readme = ""

# Finds the "README.md" file
# and reads it
with open("README.rst") as file:
    readme = file.read()

# Setups for Pypi
setup(
    name="azurlane",
    packages=["azurlane"],
    version=version,
    description="Unofficial Azur Lane API library made in Python",
    long_description=str(readme),
    author="August, Spimy",
    author_email="august@augu.dev",
    url="https://github.com/AzurAPI/azurapi-py",
    include_package_data=True,
    keywords=["azurlane", "azur lane"],
    classifiers=[
        "Programming Language :: Python :: 3.7"
    ],
    install_requires=[
        "requests"
    ]
)