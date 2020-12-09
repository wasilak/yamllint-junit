#! /usr/bin/env python
#  -*- coding: utf-8 -*-

from setuptools import setup

from yamllint_junit_bootstrap import bootstrap

version = bootstrap.__version__

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='yamllint-junit',
    packages=['yamllint_junit_bootstrap'],
    version=version,
    description='yamllint to JUnit converter.',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author='wasil',
    author_email='piotr.m.boruc@gmail.com',
    url='https://github.com/wasilak/yamllint-junit',
    download_url='https://github.com/wasilak/yamllint-junit/archive/%s.tar.gz' % version,
    keywords=['yaml', 'junit'],
    classifiers=[],
    entry_points={
        "console_scripts": ['yamllint-junit = yamllint_junit_bootstrap.bootstrap:main']
    },
    install_requires=[
        'yamllint',
    ],
    tests_require=[
        'pytest',
        'flake8',
        'coverage',
        'mock',
    ],
)
