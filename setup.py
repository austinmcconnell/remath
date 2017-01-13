#!/usr/bin/env python
# -*- coding: utf-8 -*-


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read().replace('.. :changelog:', '')

requirements = [
]

test_requirements = [
    'pytest',
    'pylint',
    'pycodetyle',
    'pydocstyle'
]

setup(
    name='remath',
    version='0.1.0',
    description="Real Estate Math contains common math equations for real estate analysis",
    long_description=readme + '\n\n' + history,
    author="Austin McConnell",
    author_email='austin.s.mcconnell@gmail.com',
    url='https://github.com/austinmcconnell/remath',
    packages=[
        'remath',
    ],
    package_dir={'remath':
                 'remath'},
    include_package_data=True,
    install_requires=requirements,
    license="ISCL",
    zip_safe=False,
    keywords='remath',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: ISC License (ISCL)',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    test_suite='tests',
    tests_require=test_requirements
)
