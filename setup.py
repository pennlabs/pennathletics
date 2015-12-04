import re

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    name='pennathletics',
    version='0.0.1',
    description='Python SDK for Penn Athletics.',
    author='Adel Qalieh',
    author_email='aqalieh95@gmail.com',
    url='http://github.com/pennlabs/pennathletics',
    license='MIT'
)
