#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim: set ts=4 sts=4 sw=4 et:
"""
@author: Wu Liang
@date: 2012-06-12 20:22
@version: 0.0.0
"""

class ErrorResponseException(Exception):
    def __init__(self, kargs=dict()):
        super(self.__class__, self).__init__()

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

    def __str__(self):
        return "%s, ErrorCode: %s" % (self.msg, self.code)
