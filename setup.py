from setuptools import find_packages,setup
from typing import List



def get_requirements()->List[str]:
    
    """
    This function will return list of requirements
    """
   
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove('-e .')
    
    return requirements
          
 


setup(
    name="sensor",
    version="0.0.1",
    author="krishnakanth",
    author_email="kgkrishnakanth7703@gmail.com",
    packages = find_packages(),
    install_requires=get_requirements()
)

