import setuptools

with open('README.md', 'r') as readme:
    long_description = readme.read()

setuptools.setup(
    name='sdk-dados-abertos-camara',
    version='0.0.7',
    author='AcompanhaLegis',
    description='SDK to use Dados Abertos da Camara dos Deputados',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/acompanhalegis/sdk-dados-abertos-camara-py',
    packages=setuptools.find_packages(),
    install_requires=['requests==2.25.1'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6'
)
