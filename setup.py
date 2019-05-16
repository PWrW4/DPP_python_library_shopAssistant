from setuptools import setup, find_packages

setup(
    name='dpp_python_library_shopAssistant',
    version='0.2.3',
    packages=find_packages(),
    license='MIT',
    description='An example python package - DPP PWr ShopAssistant',
    long_description=open('README.txt').read(),
    install_requires=['pyyaml'],
    url='https://git.e-science.pl/wwojcik235621/dpp_python_library_shopAssistant',
    author='Wojciech Wójcik',
    author_email='235621@student.pwr.edu.pl',
    include_package_data=True
)