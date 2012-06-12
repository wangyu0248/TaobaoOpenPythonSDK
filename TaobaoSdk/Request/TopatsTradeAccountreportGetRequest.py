#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim: set ts=4 sts=4 sw=4 et:



## @brief 1.提供异步下载用户支付宝对账信息接口 2.一次调用最多支持下载3个月的对账信息 3.仅能获取2010年6月10日以后的信息 4.提交任务会进行初步任务校验，如果成功会返回任务号和创建时间，如果失败就报错 5.可以接收淘宝发出的任务完成消息，也可以过一段时间来取结果。获取结果接口为taobao.topats.result.get 6.支付宝证书签名方法见文档：“http://open.taobao.com/dev/index.php/如何数字证书签名” 7.此api执行完成发送的通知消息格式为{"task":{"task_id":123456,"created":"2010-8-19"}} 8.此任务是大数据任务，获取任务结果时只能得到下载url 9.子任务结果解析见TradeAccountDetail结构体说明 10.此接口执行任务时间段为：00:00:00-09:30:00;11:00:00-14:00:00;17:00:00-20:00:00;22:30:00-23:59:59，只有在这段时间内才能返回查询结果 
# @author wuliang@maimiaotech.com
# @date 2012-06-09 16:55:54
# @version: 0.0.16

import os
import sys
import time



def __getCurrentPath():
    return os.path.normpath(os.path.join(os.path.realpath(__file__), os.path.pardir))

__modulePath = os.path.join(__getCurrentPath(), os.path.pardir)
__modulePath = os.path.normpath(__modulePath)
if __modulePath not in sys.path:
    sys.path.insert(0, __modulePath)
from Response import TopatsTradeAccountreportGetResponse


## @brief <SPAN style="font-size:16px; font-family:'宋体','Times New Roman',Georgia,Serif;">1.提供异步下载用户支付宝对账信息接口 2.一次调用最多支持下载3个月的对账信息 3.仅能获取2010年6月10日以后的信息 4.提交任务会进行初步任务校验，如果成功会返回任务号和创建时间，如果失败就报错 5.可以接收淘宝发出的任务完成消息，也可以过一段时间来取结果。获取结果接口为taobao.topats.result.get 6.支付宝证书签名方法见文档：“http://open.taobao.com/dev/index.php/如何数字证书签名” 7.此api执行完成发送的通知消息格式为{"task":{"task_id":123456,"created":"2010-8-19"}} 8.此任务是大数据任务，获取任务结果时只能得到下载url 9.子任务结果解析见TradeAccountDetail结构体说明 10.此接口执行任务时间段为：00:00:00-09:30:00;11:00:00-14:00:00;17:00:00-20:00:00;22:30:00-23:59:59，只有在这段时间内才能返回查询结果 </SPAN>
# <UL>
# <LI>
# <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">CName</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">异步获取淘宝卖家绑定的支付宝账户的财务明细</SPAN>
# </LI>
# <LI>
# <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Authorize</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">必须用户授权</SPAN>
# </LI>
# </UL>
class TopatsTradeAccountreportGetRequest(object):
    def __init__(self):
        super(self.__class__, self).__init__()
        
        ## @brief <SPAN style="font-size:16px; font-family:'宋体','Times New Roman',Georgia,Serif;">获取API名称</SPAN>
        # <UL>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Type</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">str</SPAN>
        # </LI>
        # </UL>
        self.method = "taobao.topats.trade.accountreport.get"
        
        ## @brief <SPAN style="font-size:16px; font-family:'宋体','Times New Roman',Georgia,Serif;">时间戳，如果不设置,发送请求时将使用当时的时间</SPAN>
        # <UL>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Type</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">int</SPAN>
        # </LI>
        # </UL>
        self.timestamp = int(time.time())

        
        ## @brief <SPAN style="font-size:16px; font-family:'宋体','Times New Roman',Georgia,Serif;">账务日期开始时间，时间必须大于2010-06-10 00:00:00</SPAN>
        # <UL>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Type</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">Date</SPAN>
        # </LI>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Level</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">Basic</SPAN>
        # </LI>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Required</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">必须</SPAN>
        # </LI>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Sample</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">2010-07-01 00:00:00</SPAN>
        # </LI>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Default</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">None</SPAN>
        # </LI>
        # </UL>
        self.start_created = None
        
        ## @brief <SPAN style="font-size:16px; font-family:'宋体','Times New Roman',Georgia,Serif;">账务日期查询结束时间。查询结束时间必须大于查询开始时间，并且时间跨度不能超过3个月。</SPAN>
        # <UL>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Type</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">Date</SPAN>
        # </LI>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Level</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">Basic</SPAN>
        # </LI>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Required</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">必须</SPAN>
        # </LI>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Sample</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">2010-09-01 00:00:00</SPAN>
        # </LI>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Default</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">None</SPAN>
        # </LI>
        # </UL>
        self.end_created = None
        
        ## @brief <SPAN style="font-size:16px; font-family:'宋体','Times New Roman',Georgia,Serif;">返回信息包含的字段，详情请见TradeAccountDetail结构体说明</SPAN>
        # <UL>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Type</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">Field List</SPAN>
        # </LI>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Level</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">Basic</SPAN>
        # </LI>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Required</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">必须</SPAN>
        # </LI>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Sample</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">taobao_tid,alipay_tid</SPAN>
        # </LI>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Default</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">None</SPAN>
        # </LI>
        # </UL>
        self.fields = None
