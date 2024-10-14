from setuptools import setup
import os

OPENMM_VERSION=os.getenv('OPENMM_VERSION')
HIP_VERSION=os.getenv('HIP_VERSION')

setup(
    name=f'OpenMM-HIP-{HIP_VERSION}',
    version=OPENMM_VERSION,
    description='HIP platform for OpenMM',
    author='Peter Eastman',
    url='https://openmm.org',
    packages=[]
)
