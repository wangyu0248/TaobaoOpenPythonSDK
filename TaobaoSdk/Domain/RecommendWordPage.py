#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim: set ts=4 sts=4 sw=4 et:


## @brief 一页推荐词列表
# @author wuliang@maimiaotech.com
# @date 2012-06-21 12:19:27
# @version: 0.0.0

from copy import deepcopy
from datetime import datetime
import os
import sys
import time
import types

def __getCurrentPath():
    return os.path.normpath(os.path.join(os.path.realpath(__file__), os.path.pardir))

if __getCurrentPath() not in sys.path:
    sys.path.insert(0, __getCurrentPath())


                        
from RecommendWord import RecommendWord

        
## @brief <SPAN style="font-size:16px; font-family:'宋体','Times New Roman',Georgia,Serif;">一页推荐词列表</SPAN>
class RecommendWordPage(object):
    def __init__(self, kargs=dict()):
        super(self.__class__, self).__init__()

        self.__kargs = deepcopy(kargs)
        
        
        ## @brief <SPAN style="color:Blue3; font-size:16px; font-family:'宋体','Times New Roman',Georgia,Serif;">返回第几页的数据从1开始。 如果输入的值大于可取得的最大页码值时，将返回 最大的页码值并且recommend_word_list值将 为空</SPAN>
        # <UL>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Type</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">Number</SPAN>
        # </LI>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Level</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">Basic</SPAN>
        # </LI>
        # </UL>
        self.page_no = None
        
        ## @brief <SPAN style="color:Blue3; font-size:16px; font-family:'宋体','Times New Roman',Georgia,Serif;">每页数据大小</SPAN>
        # <UL>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Type</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">Number</SPAN>
        # </LI>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Level</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">Basic</SPAN>
        # </LI>
        # </UL>
        self.page_size = None
        
        ## @brief <SPAN style="color:Blue3; font-size:16px; font-family:'宋体','Times New Roman',Georgia,Serif;">推荐词分页对象列表</SPAN>
        # <UL>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Type</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">RecommendWord</SPAN>
        # </LI>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Level</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">Object Array</SPAN>
        # </LI>
        # </UL>
        self.recommend_word_list = None
        
        ## @brief <SPAN style="color:Blue3; font-size:16px; font-family:'宋体','Times New Roman',Georgia,Serif;">所查询的数据总数</SPAN>
        # <UL>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Type</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">Number</SPAN>
        # </LI>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Level</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">Basic</SPAN>
        # </LI>
        # </UL>
        self.total_item = None
        
        self.__init(kargs)

    def toDict(self, **kargs):
        result = deepcopy(self.__kargs)
        for key, value in self.__dict__.iteritems():
            if key.endswith("__kargs"):
                continue
            if value == None:
                if kargs.has_key("includeNone") and kargs["includeNone"]:
                    result[key] = value
                else:
                    continue
            else:
                result[key] = value
        result = self.__unicodeToUtf8(result)
        return result

    def __unicodeToUtf8(self, obj):
        if isinstance(obj, types.UnicodeType):
            return obj.encode("utf-8")
        elif isinstance(obj, types.DictType):
            results = dict()
            for key, value in obj.iteritems():
                results[self.__unicodeToUtf8(key)] = self.__unicodeToUtf8(value)
            return results
        elif isinstance(obj, types.ListType):
            results = [self.__unicodeToUtf8(x) for x in obj]
            return results
        else:
            return obj
        
    def _newInstance(self, name, value):
        propertyType = self._getPropertyType(name)
        if propertyType == bool:
            return value
        elif propertyType == datetime:
            format = "%Y-%m-%d %H:%M:%S"
            return datetime.strptime(value, format)
        elif propertyType == str:
            return value.encode("utf-8")
        else:
            return propertyType(value)
        
    def _getPropertyType(self, name):
        properties = {
            
            "page_no": "Number",
            
            "page_size": "Number",
            
            "recommend_word_list": "RecommendWord",
            
            "total_item": "Number",
        }
        nameType = properties[name]
        pythonType = None
        if nameType == "Number":
            pythonType = int
        elif nameType == "String":
            pythonType = str
        elif nameType == 'Boolean':
            pythonType = bool
        elif nameType == "Date":
            pythonType = datetime
        elif nameType == 'Field List':
            pythonType == str
        elif nameType == 'Price':
            pythonType = float
        elif nameType == 'byte[]':
            pythonType = str
        else:
            pythonType = getattr(
                sys.modules[os.path.basename(
                os.path.dirname(os.path.realpath(__file__))) + "." + nameType], 
                nameType)
        return pythonType
        
    def __init(self, kargs):
        
        if kargs.has_key("page_no"):
            self.page_no = self._newInstance("page_no", kargs["page_no"])
        
        if kargs.has_key("page_size"):
            self.page_size = self._newInstance("page_size", kargs["page_size"])
        
        if kargs.has_key("recommend_word_list"):
            self.recommend_word_list = self._newInstance("recommend_word_list", kargs["recommend_word_list"])
        
        if kargs.has_key("total_item"):
            self.total_item = self._newInstance("total_item", kargs["total_item"])
