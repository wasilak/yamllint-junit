from setuptools import setup

from yamllint_junit_bootstrap import bootstrap

version = bootstrap.version()

setup(
    name='yamllint-junit',
    packages=['yamllint_junit_bootstrap'],
    version=version,
    description='yamllint to JUnit converter.',
    author='wasil',
    author_email='piotr.m.wasilewski@gmail.com',
    url='https://github.com/wasilak/yamllint-junit',
    download_url='https://github.com/wasilak/yamllint-junit/archive/%s.tar.gz'  % (version),
    keywords=['yaml', 'junit'],
    classifiers=[],
    entry_points = {
        "console_scripts": ['yamllint-junit = yamllint_junit_bootstrap.bootstrap:main']
    },
    install_requires=[
        'yamllint',
    ],
)
