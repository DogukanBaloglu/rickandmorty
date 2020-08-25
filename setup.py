from setuptools import find_packages, setup

with open('README.md') as readme_file:
    readme = readme_file.read()

setup(
    name='rickandmorty',
    author='Dogukan Baloglu',
    author_email='dogukanbaloglu99@gmail.com',
    classifiers=[
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    packages=find_packages(include=['rickandmorty'],exclude=['tests*']),
    version='0.1.0',
    description='Rick and Morty client for Rick and Morty API (https://rickandmortyapi.com/) ',
    long_description= readme ,
    long_description_contet_type='text/markdown',
    license='MIT License',
    install_requires=['requests'],
    test_require=[''],
    keywords='rickandmorty',
    url='https://github.com/DogukanBaloglu/rickandmorty'
)