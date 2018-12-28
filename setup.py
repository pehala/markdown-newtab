#!/usr/bin/python
# -*- coding: utf-8 -*-
from setuptools import setup

with open('README.md') as f:
    long_description = f.read()

setup(
    name='markdown3_newtab',
    version='0.2.0',
    description='Markdown Extension to add target="_blank" to all links.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Petr Hála',
    author_email='halapetr@selfnet.cz',
    packages=['markdown3_newtab'],
    url='https://github.com/pehala/markdown-newtab',
    license='CC0'
)
