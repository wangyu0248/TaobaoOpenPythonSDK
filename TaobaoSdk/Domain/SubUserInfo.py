#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim: set ts=4 sts=4 sw=4 et:


## @brief 子账号基本信息
# @author wuliang@maimiaotech.com
# @date 2012-06-21 17:17:30
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


                                                        
## @brief <SPAN style="font-size:16px; font-family:'宋体','Times New Roman',Georgia,Serif;">子账号基本信息</SPAN>
class SubUserInfo(object):
    def __init__(self, kargs=dict()):
        super(self.__class__, self).__init__()

        self.__kargs = deepcopy(kargs)
        
        
        ## @brief <SPAN style="color:Blue3; font-size:16px; font-family:'宋体','Times New Roman',Georgia,Serif;">子账号姓名</SPAN>
        # <UL>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Type</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">String</SPAN>
        # </LI>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Level</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">Basic</SPAN>
        # </LI>
        # </UL>
        self.full_name = None
        
        ## @brief <SPAN style="color:Blue3; font-size:16px; font-family:'宋体','Times New Roman',Georgia,Serif;">是否参与分流 1不参与 2参与</SPAN>
        # <UL>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Type</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">Number</SPAN>
        # </LI>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Level</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">Basic</SPAN>
        # </LI>
        # </UL>
        self.is_online = None
        
        ## @brief <SPAN style="color:Blue3; font-size:16px; font-family:'宋体','Times New Roman',Georgia,Serif;">子账号用户名</SPAN>
        # <UL>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Type</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">String</SPAN>
        # </LI>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Level</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">Basic</SPAN>
        # </LI>
        # </UL>
        self.nick = None
        
        ## @brief <SPAN style="color:Blue3; font-size:16px; font-family:'宋体','Times New Roman',Georgia,Serif;">子账号所属的主账号的唯一标识</SPAN>
        # <UL>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Type</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">Number</SPAN>
        # </LI>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Level</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">Basic</SPAN>
        # </LI>
        # </UL>
        self.seller_id = None
        
        ## @brief <SPAN style="color:Blue3; font-size:16px; font-family:'宋体','Times New Roman',Georgia,Serif;">主账号昵称</SPAN>
        # <UL>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Type</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">String</SPAN>
        # </LI>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Level</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">Basic</SPAN>
        # </LI>
        # </UL>
        self.seller_nick = None
        
        ## @brief <SPAN style="color:Blue3; font-size:16px; font-family:'宋体','Times New Roman',Georgia,Serif;">子账号当前状态 1正常 -1删除  2冻结</SPAN>
        # <UL>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Type</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">Number</SPAN>
        # </LI>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Level</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">Basic</SPAN>
        # </LI>
        # </UL>
        self.status = None
        
        ## @brief <SPAN style="color:Blue3; font-size:16px; font-family:'宋体','Times New Roman',Georgia,Serif;">子账号Id</SPAN>
        # <UL>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Type</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">Number</SPAN>
        # </LI>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Level</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">Basic</SPAN>
        # </LI>
        # </UL>
        self.sub_id = None
        
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
            
            "full_name": "String",
            
            "is_online": "Number",
            
            "nick": "String",
            
            "seller_id": "Number",
            
            "seller_nick": "String",
            
            "status": "Number",
            
            "sub_id": "Number",
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
        
        if kargs.has_key("full_name"):
            self.full_name = self._newInstance("full_name", kargs["full_name"])
        
        if kargs.has_key("is_online"):
            self.is_online = self._newInstance("is_online", kargs["is_online"])
        
        if kargs.has_key("nick"):
            self.nick = self._newInstance("nick", kargs["nick"])
        
        if kargs.has_key("seller_id"):
            self.seller_id = self._newInstance("seller_id", kargs["seller_id"])
        
        if kargs.has_key("seller_nick"):
            self.seller_nick = self._newInstance("seller_nick", kargs["seller_nick"])
        
        if kargs.has_key("status"):
            self.status = self._newInstance("status", kargs["status"])
        
        if kargs.has_key("sub_id"):
            self.sub_id = self._newInstance("sub_id", kargs["sub_id"])
