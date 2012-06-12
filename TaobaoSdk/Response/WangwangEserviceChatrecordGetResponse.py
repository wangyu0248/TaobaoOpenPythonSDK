#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim: set ts=4 sts=4 sw=4 et:



## @brief 该接口会返回一个聊天记录的下载地址。 请于5分钟以后使用该链接下载,该链接有如下限制： 1.该链接的有效期为3个小时，逾期作废。 2.同一链接只能使用一次。  用户点击地址，下载聊天记录压缩包（压缩包中含有1个文件或多个文件，查询了几个用户的聊天记录，就含有几个文本文件）。    备注：1、如果是操作者ID=被查者ID，返回被查者ID的"聊天记录"。      2、如果操作者是组管理员，他可以查询他的组中的所有子帐号的"聊天记录"。      3、如果操作者是主账户，他可以查询所有子帐号的"聊天记录"。     4、被查者ID可以是多个，用 "," 隔开，id数不能超过30。     5、开始时间与结束时间之间的间隔不能超过7天     6、不能查询30天以前的记录     7、不能查询当天的数据
# @author wuliang@maimiaotech.com
# @date 2012-06-09 16:56:03
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


    

## @brief <SPAN style="font-size:16px; font-family:'宋体','Times New Roman',Georgia,Serif;">Response: 该接口会返回一个聊天记录的下载地址。 请于5分钟以后使用该链接下载,该链接有如下限制： 1.该链接的有效期为3个小时，逾期作废。 2.同一链接只能使用一次。  用户点击地址，下载聊天记录压缩包（压缩包中含有1个文件或多个文件，查询了几个用户的聊天记录，就含有几个文本文件）。    备注：1、如果是操作者ID=被查者ID，返回被查者ID的"聊天记录"。      2、如果操作者是组管理员，他可以查询他的组中的所有子帐号的"聊天记录"。      3、如果操作者是主账户，他可以查询所有子帐号的"聊天记录"。     4、被查者ID可以是多个，用 "," 隔开，id数不能超过30。     5、开始时间与结束时间之间的间隔不能超过7天     6、不能查询30天以前的记录     7、不能查询当天的数据</SPAN>
# <UL>
# <LI>
# <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">CName</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">聊天记录查询</SPAN>
# </LI>
# <LI>
# <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Authorize</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">必须用户授权</SPAN>
# </LI>
# </UL>
class WangwangEserviceChatrecordGetResponse(object):
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

        
        
        ## @brief <SPAN style="font-size:16px; font-family:'宋体','Times New Roman',Georgia,Serif;">聊天日志文件下载url</SPAN>
        # <UL>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Type</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">String</SPAN>
        # </LI>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Level</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">Basic</SPAN>
        # </LI>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Required</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">true</SPAN>
        # </LI>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Sample</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">http://ltjl.wangwang.taobao.com/top/ecs/downLogFile.do?login_id=cntaobaoabc002&ts=1283262864373&r=39203bbe3bd64ff5b9ec5deb4a509221&t=8b0f6e28136274d07e155e236dbc47e7</SPAN>
        # </LI>
        # </UL>
        self.log_file_url = None
        ''' 
        @ivar log_file_url: 聊天日志文件下载url; B{Level}: C{Basic}; B{Required}: C{true}; B{Sample}: C{http://ltjl.wangwang.taobao.com/top/ecs/downLogFile.do?login_id=cntaobaoabc002&ts=1283262864373&r=39203bbe3bd64ff5b9ec5deb4a509221&t=8b0f6e28136274d07e155e236dbc47e7};
        @type log_file_url: String
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
            
            "log_file_url": "String",
        }
        levels = {
            
            "log_file_url": "Basic",
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
        
        if kargs.has_key("log_file_url"):
            self.log_file_url = self._newInstance("log_file_url", kargs["log_file_url"])
        pass