from setuptools import setup, find_packages

setup(
    name='dpp_python_library_shopAssistant',
    version='0.1',
    packages=find_packages(exclude=['tests*']),
    license='MIT',
    description='An example python package - DPP PWr ShopAssistant',
    long_description=open('README.txt').read(),
    install_requires=['pyyaml'],
    url='https://git.e-science.pl/wwojcik235621/dpp_python_library_shopAssistant',
    author='Wojciech Wójcik',
    author_email='235621@student.pwr.edu.pl'
)