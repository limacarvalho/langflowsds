from setuptools import setup, find_packages

setup(
    name="langflowsds",
    version="0.1",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[],
    entry_points={
        "console_scripts": [
            "langflowsds=langflowsds.main:main",
        ],
    },
)
