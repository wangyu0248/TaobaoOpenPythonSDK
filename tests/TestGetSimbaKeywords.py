#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim: set ts=4 sts=4 sw=4 et:
"""
@author: Wu Liang
@authors: 
@date: Jun 12, 2012 9:54:48 AM
@contact: wuliang@maimiaotech.com
@version: 0.0.0
@deprecated:
@license:
@copyright:
"""


import datetime
import os
import sys
import unittest

def __getCurrentPath():
    return os.path.normpath(os.path.join(os.path.realpath(__file__), os.path.pardir))
sys.path.insert(0, os.path.join(__getCurrentPath(), os.path.pardir))

from TaobaoSdk import TaobaoClient
from TaobaoSdk import SimbaKeywordsGetRequest
from TaobaoSdk import SimbaKeywordsGetResponse
from TaobaoSdk import Keyword

class TestGetSimbaKeywords(unittest.TestCase):
    def setUp(self):
        serverUrl = "http://gw.api.taobao.com/router/rest"
        appKey = "12651461"
        appSecret = "80a15051c411f9ca52d664ebde46a9da"
        self.client = TaobaoClient(serverUrl, appKey, appSecret)
        pass
        
    def tearDown(self):
        self.client = None
        
    def testGetSimbaKeywords(self):
        request = SimbaKeywordsGetRequest()
        request.nick = "热风旗舰店"
        request.adgroup_id = "110581370"
        responses = None
        while responses == None:
            responses = self.client.execute(request, 
                    #    "62029014bdfcaeddf5042fb3a9112165e252fa9f1034277106852163")
            "62029014bdfcaeddf5042fb3a9112165e252fa9f1034277106852162")
        response = responses[0]
        assert isinstance(response,SimbaKeywordsGetResponse)
        for keyword in response.keywords:
            print keyword.word
        print response.responseBody


if __name__ == '__main__':
    unittest.main()
