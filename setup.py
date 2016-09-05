"""A setuptools based setup module.

See:
https://packaging.python.org/en/latest/distributing.html
https://github.com/pypa/sampleproject
"""

from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='multimodule',
    version='0.8.0',
    description='Create a single module that interfaces multiple.',
    long_description=long_description,
    url='https://github.com/jbwinters/multimodule',
    author='Josh Winters',
    author_email='josh@idealspot.com',
    license='GNU GPL',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Software Development :: Libraries :: Python Modules',
        'License :: OSI Approved :: GNU General Public License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    keywords='framework versioning',
    packages=find_packages(exclude=['contrib', 'docs', 'tests']),
)
