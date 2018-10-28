#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""skserialize setup file."""

import sys

try:
    from setuptools import setup, find_packages
except ImportError:
    print('Please install or upgrade setuptools or pip to continue')
    sys.exit(1)

import skserialize

setup(
    name='skserialize',
    packages=find_packages(),
    description='Efficient, safe sklearn model persistence',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    download_url='https://github.com/nielstron/skserialize/tarball/master',
    version=skserialize.__version__,
    url=skserialize.__url__,
    author=skserialize.__author__,
    author_email=skserialize.__author_email__,
    license=skserialize.__license__,
    keywords=[
    ],
    install_requires=['tables'],
    classifiers=[
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX', 'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.6',
        'Development Status :: 3 - Alpha',
    ])
