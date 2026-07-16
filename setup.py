from setuptools import setup, find_packages
from typing import List
def get_requirements(file_path) -> List[str]:
    HYPHEN_E_DOT = '-e .'
    requirements=[]
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n", "") for req in requirements]
        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)
        return requirements




setup(
    name='ml_project',
    version='0.1.0',
    packages=find_packages(),
    author='zain ul abideen',
    email="zainulabideenab9@gmail.com",
    install_requires=get_requirements('requirements.txt')
)