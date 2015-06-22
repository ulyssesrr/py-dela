#!/usr/bin/env python3
from setuptools import setup

def readme():
    with open('README.md') as f:
        return f.read()


setup(name='py-dela',
      version='0.2.0',
      description='Python DELA Dictionary(Unitex) support library',
      long_description=readme(),
      author='Ulysses Rangel Ribeiro',
      author_email='ulyssesrr@gmail.com',
      maintainer='Daniel Blanchard',
      maintainer_email='dblanchard@ets.org',
      url='https://github.com/ulyssesrr/py-dela',
      license="LGPL",
      keywords=['dela', 'unitex', 'lemmatization'],
      classifiers=["Development Status :: 3 - Alpha",
                   "Intended Audience :: Developers",
                   ("License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)"),
                   "Operating System :: OS Independent",
                   "Programming Language :: Python",
                   'Programming Language :: Python :: 3',
                   'Programming Language :: Python :: 3.2',
                   'Programming Language :: Python :: 3.3',
                   'Programming Language :: Python :: 3.4',
                   ("Topic :: Software Development :: Libraries :: Python "
                    "Modules"),
                   "Topic :: Text Processing :: Linguistic"],
      packages=['pydela'])