from setuptools import setup, find_packages

setup(
    name='pyrawfdw',
    version='0.0.0',
    description='',
    author='Miguel Branco',
    author_email='miguel.branco@epfl.ch',
    packages=find_packages(),
    install_requires = [
        'multicorn',
        'pyrawcore',
    ]
)
