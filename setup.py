import re

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

version = ''
with open('pennathletics/__init__.py', 'r') as fd:
    version = re.search(r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]',
                        fd.read(), re.MULTILINE).group(1)

with open('README.md', 'r', 'utf-8') as f:
    readme = f.read()

setup(
    name='pennathletics',
    version=version,
    description='Python SDK for Penn Athletics.',
    long_description=readme,
    author='Adel Qalieh',
    author_email='aqalieh95@gmail.com',
    url='http://github.com/pennlabs/pennathletics',
    license='MIT'
)
