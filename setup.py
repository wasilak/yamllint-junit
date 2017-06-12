from distutils.core import setup
setup(
    name='yamllint-junit',
    packages=['yamllint-junit'],
    version='0.1',
    description='yamllint to JUnit converter.',
    author='wasil',
    author_email='piotr.m.wasilewski@gmail.com',
    url='https://github.com/wasilak/yamllint-junit',
    download_url='https://github.com/wasilak/yamllint-junit/archive/0.5.tar.gz',
    keywords=['ansible', 'junit'],
    classifiers=[],
    scripts=['bin/yamllint-junit'],
    install_requires=[
        'yamllint',
    ]
)
