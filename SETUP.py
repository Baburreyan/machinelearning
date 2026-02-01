from setuptools import find_packages, setup
from typing import List

def get_requirements(file_path: str) -> List[str]:
    '''This function returns the list of requirements from a file'''
    requirements = []
    with open(file_path) as file_obj:
        # Corrected: Added 'in' keyword and handled newlines
        requirements = file_obj.readlines()
        requirements = [req.replace("\n", "") for req in requirements]
        
        # Standard practice: Remove '-e .' if present in requirements.txt
        if "-e ." in requirements:
            requirements.remove("-e .")
            
    return requirements # Added: Essential to return the list

setup(
    name="machinelearning",
    version="0.0.1",
    author="krish",
    author_email="baburreyan123@gmail.com", # Corrected spelling & added comma
    packages=find_packages(),               # Added comma
    install_requires=get_requirements("requirements.txt") # Corrected function name
)