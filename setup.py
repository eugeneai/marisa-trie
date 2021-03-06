#! /usr/bin/env python
"""Static memory-efficient and fast Trie-like structures for Python."""

import glob
import itertools

from setuptools import setup, Extension

MARISA_DIR = "lib"
MARISA_FILES = [
    "lib/marisa/*.cc",
    "lib/marisa/grimoire.cc",
    "lib/marisa/grimoire/io/*.cc",
    "lib/marisa/grimoire/trie/*.cc",
    "lib/marisa/grimoire/vector/*.cc",
]

MARISA_FILES = list(itertools.chain(*(glob.glob(path) for path in MARISA_FILES)))

DESCRIPTION = __doc__
LONG_DESCRIPTION = open("README.rst").read() + open("CHANGES.rst").read()
LICENSE = "MIT"

CLASSIFIERS = [
    "Development Status :: 4 - Beta",
    "Intended Audience :: Developers",
    "Intended Audience :: Science/Research",
    "License :: OSI Approved :: MIT License",
    "Programming Language :: Cython",
    "Programming Language :: Python",
    "Programming Language :: Python :: 2",
    "Programming Language :: Python :: 2.6",
    "Programming Language :: Python :: 2.7",
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3.4",
    "Programming Language :: Python :: 3.5",
    "Programming Language :: Python :: Implementation :: CPython",
    "Topic :: Software Development :: Libraries :: Python Modules",
    "Topic :: Scientific/Engineering :: Information Analysis",
    "Topic :: Text Processing :: Linguistic",
]

setup(name="marisa-trie",
      version="0.7.2",
      description=DESCRIPTION,
      long_description=LONG_DESCRIPTION,
      author="Mikhail Korobov",
      author_email="kmike84@gmail.com",
      license=LICENSE,
      url="https://github.com/kmike/marisa-trie",
      classifiers=CLASSIFIERS,
      libraries=[("marisa", {
          "sources": MARISA_FILES,
          "include_dirs": [MARISA_DIR]
      })],
      ext_modules=[
          Extension("marisa_trie", [
              "src/agent.cpp",
              "src/base.cpp",
              "src/iostream.cpp",
              "src/key.cpp",
              "src/keyset.cpp",
              "src/marisa_trie.cpp",
              "src/query.cpp",
              "src/std_iostream.cpp",
              "src/trie.cpp"
          ], include_dirs=[MARISA_DIR])
      ],

      setup_requires=["pytest-runner"],
      tests_require=["pytest", "hypothesis==2.0"])
