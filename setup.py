from setuptools import setup
from setuptools import find_packages


def readme():
    with open("README.md") as f:
        return f.read()


def required():
    with open("requirements.txt") as f:
        return f.read().splitlines()


setup(
    name="scheduler",
    version="0.0.1",
    description="A schedule app",
    long_description=readme(),
    long_description_content_type="text/markdown",
    keywords="schedule",
    author="André P. Santos",
    author_email="andreztz@gmail.com",
    url="https://github.com/andreztz/schedule",
    license="MIT",
    packages=find_packages(),
    install_requires=required(),
    entry_points={
        "gui_scripts": ["tkscheduler=core.__main__:main"],
        "console_scripts": ["scheduler=core.script:main"],
    },
    classifiers=[
        "Development Status :: 1 - Planning",
        "Programming Language :: Python :: 3",
    ],
)
