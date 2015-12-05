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
    license='MIT',
    packages=['pennathletics'],
    install_requires=[
        'beautifulsoup4==4.4.1',
        'requests==2.8.1',
        'six==1.10.0'
    ]
)
