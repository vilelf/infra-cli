from setuptools import setup


setup(
    name='infra-cli',
    version='0.1',
    install_requires=[
        'click',
        'requests'
    ],
    entry_points='''
        [console_scripts]
        infra-cli=main:cli
    ''',
    author='vilelf'
)