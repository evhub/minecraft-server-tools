import setuptools


setuptools.setup(
    name="minecraft-server-tools",
    version="0.0.2",
    description="Utilities for easily working with and managing minecraft forge servers.",
    url="https://github.com/evhub/minecraft-server-tools",
    author="Evan Hubinger",
    author_email="evanjhub@gmail.com",
    packages=setuptools.find_packages(),
    install_requires=[
        "requests",
        "jsoncomment",
        "tqdm",
        "psutil",
    ],
)
