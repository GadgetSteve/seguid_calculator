#!/usr/bin/env python
# -*- coding: utf-8 -*-

import versioneer
versioneer.VCS = 'git'
versioneer.versionfile_source = 'seguid_calculator/_version.py'
versioneer.versionfile_build = 'seguid_calculator/_version.py'
versioneer.tag_prefix = '' # tags are like 1.2.0
versioneer.parentdir_prefix = '' # dirname like 'myproject-1.2.0'

# Read author etc..
for line in open('seguid_calculator/__init__.py'):
    if line.startswith('__') and not line.startswith('__version') and not line.startswith('__long'):
        exec(line.strip())

from setuptools import setup

setup(  name='seguid_calculator',
        version=versioneer.get_version()[:5],
        cmdclass=versioneer.get_cmdclass(),
        author          =__author__,
        author_email    =__email__,
        packages=['seguid_calculator'],
        entry_points = { 'console_scripts': [ 'seguid_calculator = seguid_calculator.seguid:main' ]},
        url='http://pypi.python.org/pypi/seguid_calculator',
        license='LICENSE.txt',
        description='''Calculate SEGUID & cSEGUID of biological sequences''',
        long_description=open('README.rst').read(),
        install_requires =[],
        test_suite="run_tests.load_my_tests",
        zip_safe = False,
        keywords = "bioinformatics",
        classifiers = ['Development Status :: 3 - Alpha',
                       'Environment :: Console',
                       'Intended Audience :: Education',
                       'Intended Audience :: Science/Research',
                       'License :: OSI Approved :: BSD License',
                       'Programming Language :: Python :: 2.7',
                       'Topic :: Education',
                       'Topic :: Scientific/Engineering :: Bio-Informatics',])
