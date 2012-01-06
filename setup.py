#!/usr/bin/env python

from setuptools import setup

setup(name="corndog",
      version="0.0.1",
      description="Smart Redis command and control",
      author="Alex Ezell",
      author_email="aezell@gmail.com",
      install_requires=['redis==2.4.10'],
      scripts=["scripts/corndog"])
