import setuptools


setuptools.setup(
    name="minecraft-server-tools",
    version="0.0.1",
    description="A bunch of utilities for easily working with and managing minecraft servers, specifically aimed at forge servers and curseforge modpack management.",
    url="https://github.com/evhub/minecraft-server-tools",
    author="Evan Hubinger",
    author_email="evanjhub@gmail.com",
    packages=setuptools.find_packages(),
    install_requires=[
        "requests",
    ],
)
