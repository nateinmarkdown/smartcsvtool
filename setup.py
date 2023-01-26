from setuptools import setup, find_packages

setup(
    name='smartcsvtool',
    version='1.0',
    packages=find_packages(),
    url='https://github.com/nate-projects/smartcsvtool',
    author='Nate',
    author_email='2b2t@mail.com',
    description='A package for working with CSV files',
    install_requires=['pandas']
)
