#!/usr/bin/env python
from setuptools import find_packages, setup

setup(
    name='microservice-QTIP-benchmarker',
    version='0.0.1',
    description='Platform Performance Benchmarking',
    packages=find_packages(),
    install_requires=[
        'nameko==2.6.0'
    ],
    zip_safe=True
)