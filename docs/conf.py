# Copyright (c) Moshe Zadka
# See LICENSE for details.
import os
import sys

up = os.path.dirname(os.path.dirname(__file__))
sys.path.append(up)

import howsit

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.viewcode',
    'sphinx.ext.napoleon',
]
master_doc = 'index'
project = 'Howsit'
copyright = '2017, Moshe Zadka'
author = 'Moshe Zadka'
version = release = howsit.__version__
