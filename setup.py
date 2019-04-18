import pathlib
from setuptools import find_packages, setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

setup(
    name='stronk',
    version='1.1.2',
    description='Strong key generator',
    long_description=README,
    long_description_content_type="text/markdown",
    url='https://github.com/brianrthompson/stronk',
    author='Brian Thompson',
    author_email='brianrt23@gmail.com',
    license='MIT',
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6"
    ],
    packages=find_packages(exclude=("test",)),
    include_package_data=True,
    entry_points={
        "console_scripts": [
            "stronk=stronk.__main__:main",
        ]
    },
)
