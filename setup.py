from setuptools import setup

# Gets the requirements
def get_requirements():
    with open("requirements.txt") as f:
        requirements = f.read().splitlines()

    return requirements

# The version number
version = "1.0.0"

# README
readme = ""

# Finds the "README.md" file
# and reads it
with open("README.md") as file:
    readme = file.read()

# Setups for Pypi
setup(
    name="azurapi",
    packages=["azurapi"],
    version=version,
    description="Unofficial Azur Lane API library made in Python",
    long_description=str(readme),
    author="August",
    author_email="ohlookitsaugust@gmail.com",
    url="https://github.com/AzurAPI/azurapi-py",
    include_package_data=True,
    keywords=["azurlane", "azur lane"],
    install_requires=get_requirements(),
    classifiers=[
        "Programming Language :: Python :: 3.7"
    ]
)