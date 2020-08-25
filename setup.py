from setuptools import find_packages, setup

with open('README.md') as readme_file:
    readme = readme_file.read()

setup(
    name='rickandmorty',
    author='Dogukan Baloglu',
    author_email='dogukanbaloglu99@gmail.com',
    packages=find_packages(include=['rickandmorty'],exclude=['tests*']),
    version='0.1.0',
    description='Rick and Morty client for Rick and Morty API (https://rickandmortyapi.com/) ',
    detailed_description= readme ,
    license='MIT License',
    install_requires=['requests'],
    test_require=[''],
    keywords='rickandmorty',
    url='https://github.com/DogukanBaloglu/rickandmorty'
)