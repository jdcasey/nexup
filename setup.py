#!/usr/bin/env python2

from setuptools import setup, find_packages
import sys

# handle python 3
if sys.version_info >= (3,):
    use_2to3 = True
else:
    use_2to3 = False

version='0.0.1'

f = open('README.rst')
long_description = f.read().strip()
long_description = long_description.split('split here', 1)[1]
f.close()

test_deps=[
    "Mock",
    "nose",
    "responses",
  ]

extras = {
  'test':test_deps,
  'build':['tox'],
  'ci':['coverage']
}

setup(
    use_2to3=use_2to3,
    name='nexup',
    version=version,
    long_description=long_description,
    classifiers=[
      "Development Status :: 3 - Alpha",
      "Intended Audience :: Developers",
      "License :: OSI Approved :: GNU General Public License (GPL)",
      "Programming Language :: Python :: 2",
      "Programming Language :: Python :: 3",
      "Topic :: Software Development :: Build Tools",
      "Topic :: Utilities",
    ],
    keywords='nexus maven build java ',
    author='John Casey',
    author_email='jdcasey@commonjava.org',
    url='https://github.com/release-engineering/nexup',
    license='GPLv3+',
    packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
      "requests",
      "lxml",
      "click",
      "PyYAML"
    ],
    tests_require=test_deps,
    extras_require=extras,
    test_suite="tests",
    entry_points={
      'console_scripts': [
        'nexup-push = nexup:push',
        'nexup-rollback = nexup:rollback',
      ],
    }
)
