from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT='-e .'
def get_requirements(fine_path:str)->List[str]:
    '''
    This function will return list of requirements
    '''
    requirements=[]
    with open('requirements.txt') as file:
        requirements=file.readlines()
        requirements=[req.replace('\n','') for req in requirements]
        
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

        return requirements

setup(
name='mlproject',
version='0.0.1',
author='Ritika',
author_email='ritika.papai@gmail.com',
packages=find_packages(),
install_requires=get_requirements('requirements.txt')

)

