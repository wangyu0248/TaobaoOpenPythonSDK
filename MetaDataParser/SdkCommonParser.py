#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim: set ts=4 sts=4 sw=4 et:
"""
@author: Wu Liang
@authors: 
@date: Jun 12, 2012 11:48:50 AM
@contact: wuliang@maimiaotech.com 
@version: 0.0.0
@deprecated:
@license:
@copyright:
"""

from Common import *
from Settings import *

class SdkCommonParser(object):
    def __init__(self, root, output):
        self.root = root
        self.output = output
        
    def generateFiles(self):
        if not os.path.exists(self.output):
            os.makedirs(self.output)
        templateFile = Template(file(sdkCommonTemplate).read().decode("utf-8"))
        rendered = templateFile.render_unicode(root=self.root).encode("utf-8")
        fout = file(os.path.join(self.output, sdkCommonOutput), "w")
        fout.write(rendered)
        fout.close()
        
        
