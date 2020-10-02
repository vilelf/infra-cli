from setuptools import setup


setup(
    name='infra-cli',
    version='0.1',
    install_requires=[
        'click'
    ],
    entry_points='''
        [console_scripts]
        infra-cli=main:main
    ''',
    author='vilelf'
)