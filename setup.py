from setuptools import setup, find_packages

setup(
    name="bomb-library",
    version="0.0.1",
    author="Ann",
    author_email="<anastasiatrifan@gmail.com>",
    url="",
    description="calculate number of trees",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],

    entry_points={"console_scripts": ["bomb-library = bomb-library.main:download"]},
)
