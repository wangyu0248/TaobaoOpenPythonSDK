#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim: set ts=4 sts=4 sw=4 et:



## @brief * 添加邮费模板     * 新增的邮费模板属于当前会话用户     * postage_mode_types、postage_mode_dests、postage_mode_prices、 postage_mode_increases四个字段组合起来表示邮费的子模板列表。每个邮费子模板都包含了type（邮费类型，有post、 express、ems可以选择）、dest（邮费模板应用地区，每个模板可以使用于多个地区，每个地区填入他的代码，地区与地区之间用半角逗号分隔）、 price（邮费基价）、increment（邮费增价）四个部分。如果有多个子模板，则将他们的4个部分分别组合，之间用半角分号隔开（注意每个模板的每个部分的位置要一样。即，子模板1号的type、dest、price、increment都要排在这四个参数的第一位；子模板2号要排在第二位……以此类推）
# @author wuliang@maimiaotech.com
# @date 2012-06-09 16:55:58
# @version: 0.0.16

from datetime import datetime
import os
import sys
import time

def __getCurrentPath():
    return os.path.normpath(os.path.join(os.path.realpath(__file__), os.path.pardir))
    
__parentPath = os.path.normpath(os.path.join(__getCurrentPath(), os.path.pardir))
if __parentPath not in sys.path:
    sys.path.insert(0, __parentPath)


    
from Domain.Postage import Postage



## @brief <SPAN style="font-size:16px; font-family:'宋体','Times New Roman',Georgia,Serif;">Response: * 添加邮费模板     * 新增的邮费模板属于当前会话用户     * postage_mode_types、postage_mode_dests、postage_mode_prices、 postage_mode_increases四个字段组合起来表示邮费的子模板列表。每个邮费子模板都包含了type（邮费类型，有post、 express、ems可以选择）、dest（邮费模板应用地区，每个模板可以使用于多个地区，每个地区填入他的代码，地区与地区之间用半角逗号分隔）、 price（邮费基价）、increment（邮费增价）四个部分。如果有多个子模板，则将他们的4个部分分别组合，之间用半角分号隔开（注意每个模板的每个部分的位置要一样。即，子模板1号的type、dest、price、increment都要排在这四个参数的第一位；子模板2号要排在第二位……以此类推）</SPAN>
# <UL>
# <LI>
# <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">CName</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">添加邮费模板</SPAN>
# </LI>
# <LI>
# <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Authorize</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">必须用户授权</SPAN>
# </LI>
# </UL>
class PostageAddResponse(object):
    def __init__(self, kargs=dict()):
        super(self.__class__, self).__init__()
        
        
        ## @brief <SPAN style="font-size:16px; font-family:'宋体','Times New Roman',Georgia,Serif;">请求的返回信息,包含状态等</SPAN>
        # <UL>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Type</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">dict</SPAN>
        # </LI>
        # </UL>
        self.responseStatus = None

        ## @brief <SPAN style="font-size:16px; font-family:'宋体','Times New Roman',Georgia,Serif;">请求的响应内容</SPAN>
        # <UL>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Type</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">str</SPAN>
        # </LI>
        # </UL>        
        self.responseBody = None

        
        
        ## @brief <SPAN style="font-size:16px; font-family:'宋体','Times New Roman',Georgia,Serif;">新增的商品信息</SPAN>
        # <UL>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Type</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">Postage</SPAN>
        # </LI>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Level</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">Object</SPAN>
        # </LI>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Required</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">true</SPAN>
        # </LI>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Sample</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;"></SPAN>
        # </LI>
        # </UL>
        self.postage = None
        ''' 
        @ivar postage: 新增的商品信息; B{Level}: C{Object}; B{Required}: C{true}; B{Sample}: C{};
        @type postage: Postage
        '''
    
        self.__init(kargs)
    
    def _newInstance(self, name, value):
        types = self._getPropertyType(name)
        propertyType = types[0]
        isArray = types[1]
        if propertyType == bool:
            if isArray:
                return [x for x in value[value.keys()[0]]]
            else:
                return value
        elif propertyType == datetime:
            format = "%Y-%m-%d %H:%M:%S"
            if isArray:
                return [datetime.strptime(x, format) for x in value[value.keys()[0]]]
            else:
                return datetime.strptime(value, format)
        elif propertyType == str:
            if isArray:
                return [x.encode("utf-8") for x in value[value.keys()[0]]]
            else:
                return value.encode("utf-8")
        else:
            if isArray:
                return [propertyType(x) for x in value[value.keys()[0]]]
            else:
                return propertyType(value)
        
    def _getPropertyType(self, name):
        properties = {
            
            "postage": "Postage",
        }
        levels = {
            
            "postage": "Object",
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
            pythonType = getattr(sys.modules["Domain.%s" % nameType], nameType)
        
        # 是单个元素还是一个对象
        level = levels[name]
        if "Array" in level:
            return (pythonType, True)
        else:
            return (pythonType, False)

    def __init(self, kargs):
        
        if kargs.has_key("postage"):
            self.postage = self._newInstance("postage", kargs["postage"])
        pass