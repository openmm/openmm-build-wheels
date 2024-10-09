from setuptools import setup
import os

OPENMM_VERSION=os.getenv('OPENMM_VERSION')
CUDA_VERSION=os.getenv('CUDA_VERSION')

setup(
    name=f'OpenMM-CUDA-{CUDA_VERSION}',
    version=OPENMM_VERSION,
    description='CUDA platform for OpenMM',
    author='Peter Eastman',
    url='https://openmm.org',
    packages=[]
)
