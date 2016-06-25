#!/bin/env python
"""
Limf
----
Limf is a tool for uploading files to pomf.se clones.
"""
from setuptools import setup


setup(
    name='limf',
    version='0.6.0',
    url='http://github.com/lich/limf',
    license='MIT',
    author='Mikolaj \'lich\' Halber',
    author_email='lich@openmailbox.com',
    description='A tool for uploading files to pomf.se clones',
    long_description='Just read README.md. I will create .rst file when I want to do it.',
    packages=['limf'],
    install_requires=[
        'Requests>=2.6.0',
    ],
    classifiers=[
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
    ],
    entry_points={
        'console_scripts': ['limf=limf.cli:main']}
)



