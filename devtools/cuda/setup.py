from setuptools import setup
import os

OPENMM_VERSION=os.getenv('OPENMM_VERSION')
CUDA_VERSION=os.getenv('CUDA_VERSION')
if CUDA_VERSION == '12':
    CUDA_SUFFIX = '-cu12'
else:
    CUDA_SUFFIX = '>=13,<14'
setup(
    name=f'OpenMM-CUDA-{CUDA_VERSION}',
    version=OPENMM_VERSION,
    description='CUDA platform for OpenMM',
    author='Peter Eastman',
    url='https://openmm.org',
    packages=[],
    install_requires=[f'nvidia-cuda-runtime{CUDA_SUFFIX}',
                      f'nvidia-cuda-nvcc{CUDA_SUFFIX}',
                      f'nvidia-cuda-nvrtc{CUDA_SUFFIX}',
                      f'nvidia-cuda-cupti{CUDA_SUFFIX}',
                      f'nvidia-cufft{CUDA_SUFFIX}'],
    dependency_links=['https://pypi.ngc.nvidia.com']
)
