from setuptools import find_packages,setup
from typing import List

def get_packages():

    package_lst:List[str]=[]

    try:
        with open('requirements.txt','r') as file:
            lines=file.readlines()
            for line in lines:
                requirement=line.strip()
                if requirement and requirement!='-e .':
                    package_lst.append(requirement)
    except FileNotFoundError:
        print("Requirements.txt is not found")

    return package_lst

setup(
    name="NetworkSecurity",
    version="0.0.1",
    author="Arpit Shourya",
    author_email="arpitshourya2233@gmail.com",
    packages=find_packages(),
    install_requires=get_packages()
)