#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim: set ts=4 sts=4 sw=4 et:
"""
@author: Wu Liang
@authors: 
@date: 11:46:48 PM Jun 4, 2012
@contact: wuliang@maimiaotech.com
@version: 0.0.0
@deprecated:
@license:
@copyright:
"""

import os
import sys
import warnings
warnings.filterwarnings("ignore")

def __getCurrentPath():
    return os.path.normpath(os.path.join(os.path.realpath(__file__), os.path.pardir))
sys.path.insert(0, os.path.join(__getCurrentPath(), "libs", 'pytoolkit.zip'))

from ArgumentParser import ArgumentParser
from BaseClass import BaseClass
import chardet
from ConfigParser import ConfigParser
from Colorful import *
import copy
from Decoder import Decoder
import hashlib
import httplib2
import JSONLib
from mako.template import Template
import re
if float(sys.version[:3]) <= 2.4:
    from sets import Set as set
import shutil
import subprocess
import tarfile
import tempfile
import threading
import time
import urllib
import urllib2
import urlparse
import yaml
from Utility import *
import unittest
import xml.dom.minidom 