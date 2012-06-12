#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim: set ts=4 sts=4 sw=4 et:
"""
@author: Wu Liang
@authors: 
@date: Jun 12, 2012 7:11:40 PM
@contact: wuliang@maimiaotech.com
@version: 0.0.0
@deprecated:
@license:
@copyright:
"""

from datetime import datetime
import os
import sys
import time

def __getCurrentPath():
    return os.path.normpath(os.path.join(os.path.realpath(__file__), os.path.pardir))
    
__parentPath = os.path.normpath(os.path.join(__getCurrentPath(), os.path.pardir))
if __parentPath not in sys.path:
    sys.path.insert(0, __parentPath)
    
class ErrorResponse(object):
    def __init__(self, kargs=dict()):
        super(self.__class__, self).__init__()

        self.responseStatus = None

        self.responseBody = None
        
        self.code = None
        '''
        错误类型
        '''
        
        self.msg = None
        '''
        错误消息
        '''


        if kargs.has_key("code"):
            self.code = kargs["code"]
        if kargs.has_key("msg"):
            self.msg = kargs["msg"]
