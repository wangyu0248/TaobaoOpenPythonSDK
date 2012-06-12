#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim: set ts=4 sts=4 sw=4 et:


## @brief 获取单笔交易的详细信息 1.只有在交易成功的状态下才能取到交易佣金，其它状态下取到的都是零或空值  2.只有单笔订单的情况下Trade数据结构中才包含商品相关的信息  3.获取到的Order中的payment字段在单笔子订单时包含物流费用，多笔子订单时不包含物流费用  注：包含以下字段的返回会增加TOP的后台压力，请仅在确实需要的情况下才去获取：commission_fee, buyer_alipay_no, seller_alipay_no, buyer_email, seller_mobile, seller_phone, seller_name, seller_email, timeout_action_time, item_memo, trade_memo, title, available_confirm_fee
# @author wuliang@maimiaotech.com
# @date 2012-06-12 20:51:09
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


    
from Domain.Trade import Trade



## @brief <SPAN style="font-size:16px; font-family:'宋体','Times New Roman',Georgia,Serif;">Response: 获取单笔交易的详细信息 1.只有在交易成功的状态下才能取到交易佣金，其它状态下取到的都是零或空值  2.只有单笔订单的情况下Trade数据结构中才包含商品相关的信息  3.获取到的Order中的payment字段在单笔子订单时包含物流费用，多笔子订单时不包含物流费用  注：包含以下字段的返回会增加TOP的后台压力，请仅在确实需要的情况下才去获取：commission_fee, buyer_alipay_no, seller_alipay_no, buyer_email, seller_mobile, seller_phone, seller_name, seller_email, timeout_action_time, item_memo, trade_memo, title, available_confirm_fee</SPAN>
# <UL>
# </UL>
class TradeFullinfoGetResponse(object):
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

        
        
        ## @brief <SPAN style="font-size:16px; font-family:'宋体','Times New Roman',Georgia,Serif;">搜索到的交易信息列表，返回的Trade和Order中包含的具体信息为入参fields请求的字段信息</SPAN>
        # <UL>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Type</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">Trade</SPAN>
        # </LI>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Level</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">Object</SPAN>
        # </LI>
        # </UL>
        self.trade = None
    
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
            
            "trade": "Trade",
        }
        levels = {
            
            "trade": "Object",
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
        
        if kargs.has_key("trade"):
            self.trade = self._newInstance("trade", kargs["trade"])
        pass
