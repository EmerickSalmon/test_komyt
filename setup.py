from setuptools import setup, find_packages

setup(
    name='vmware-cli',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'pyvmomi',
        'rich'
    ],
)
