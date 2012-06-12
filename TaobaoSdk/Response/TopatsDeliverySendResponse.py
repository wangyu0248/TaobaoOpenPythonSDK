#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim: set ts=4 sts=4 sw=4 et:


## @brief 使用指南：http://open.taobao.com/dev/index.php/ATS%E4%BD%BF%E7%94%A8%E6%8C%87%E5%8D%97 1.提供异步批量物流发货功能 2.一次最多发货40个订单 3.提交任务会进行初步任务校验，如果成功会返回任务号和创建时间，如果失败就报错 4.可以接收淘宝发出的任务完成消息，也可以过一段时间来取结果。获取结果接口为taobao.topats.result.get 5.此api执行完成发送的通知消息格式为{"task":{"task_id":123456,"created":"2010-8-19"}}
# @author wuliang@maimiaotech.com
# @date 2012-06-12 20:51:10
# @version: 0.0.0

from datetime import datetime
import os
import sys
import time

def __getCurrentPath():
    return os.path.normpath(os.path.join(os.path.realpath(__file__), os.path.pardir))
    
__parentPath = os.path.normpath(os.path.join(__getCurrentPath(), os.path.pardir))
if __parentPath not in sys.path:
    sys.path.insert(0, __parentPath)


    
from Domain.Task import Task



## @brief <SPAN style="font-size:16px; font-family:'宋体','Times New Roman',Georgia,Serif;">Response: 使用指南：http://open.taobao.com/dev/index.php/ATS%E4%BD%BF%E7%94%A8%E6%8C%87%E5%8D%97 1.提供异步批量物流发货功能 2.一次最多发货40个订单 3.提交任务会进行初步任务校验，如果成功会返回任务号和创建时间，如果失败就报错 4.可以接收淘宝发出的任务完成消息，也可以过一段时间来取结果。获取结果接口为taobao.topats.result.get 5.此api执行完成发送的通知消息格式为{"task":{"task_id":123456,"created":"2010-8-19"}}</SPAN>
# <UL>
# </UL>
class TopatsDeliverySendResponse(object):
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

        
        
        ## @brief <SPAN style="font-size:16px; font-family:'宋体','Times New Roman',Georgia,Serif;">创建任务信息。里面只包含task_id和created</SPAN>
        # <UL>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Type</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">Task</SPAN>
        # </LI>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Level</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">Object</SPAN>
        # </LI>
        # </UL>
        self.task = None
    
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
            
            "task": "Task",
        }
        levels = {
            
            "task": "Object",
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
        
        if kargs.has_key("task"):
            self.task = self._newInstance("task", kargs["task"])
        pass
