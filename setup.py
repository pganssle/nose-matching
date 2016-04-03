#!/usr/bin/env python

from setuptools import setup

from nose_matching import __version__ as VERSION

setup(name="nose-matching",
      version=VERSION,
      description="Nose plugin allowing granular test filtering",
      author="Paul Ganssle",
      license="MIT",
      packages=['nose_matching'],
      install_requires=['nose'],
      entry_points={
        'nose.plugins.0.10':
          ['nose-matching = nose_matching.plugin:Matching']
      },
      zip_safe=True,
      classifiers=[
          'Intended Audience :: Developers',
          'License :: OSI Approved :: MIT License',
          'Operating System :: OS Independent',
          'Programming Language :: Python',
          'Programming Language :: Python :: 2',
          'Programming Language :: Python :: 2.6',
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.2',
          'Programming Language :: Python :: 3.3',
          'Programming Language :: Python :: 3.4',
          'Programming Language :: Python :: 3.5',
          'Topic :: Software Development :: Libraries',
          'Topic :: Software Development :: Testing',
          'Environment :: Console',
      ],
)
