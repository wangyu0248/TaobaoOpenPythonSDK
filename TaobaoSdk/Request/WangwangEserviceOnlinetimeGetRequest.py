#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim: set ts=4 sts=4 sw=4 et:


## @brief 描述：根据客服ID和日期，获取该客服"当日在线时长"。  备注：1、如果是操作者ID=被查者ID，返回被查者ID的"当日在线时长"。      2、如果操作者是组管理员，他可以查询他的组中的所有子帐号的"当日在线时长"。      3、如果操作者是主账户，他可以查询所有子帐号的"当日在线时长"。     4、被查者ID可以是多个，用 "," 隔开，id数不能超过30。     5、日累计在线时长定义：当日该用户累计的旺旺在线时长      6、开始时间与结束时间之间的间隔不能超过7天     7、不能查询90天以前的数据     8、不能查询当天的记录
# @author wuliang@maimiaotech.com
# @date 2012-06-21 17:17:42
# @version: 0.0.0

import os
import sys
import time



def __getCurrentPath():
    return os.path.normpath(os.path.join(os.path.realpath(__file__), os.path.pardir))

__modulePath = os.path.join(__getCurrentPath(), os.path.pardir)
__modulePath = os.path.normpath(__modulePath)
if __modulePath not in sys.path:
    sys.path.insert(0, __modulePath)


## @brief <SPAN style="font-size:16px; font-family:'宋体','Times New Roman',Georgia,Serif;">描述：根据客服ID和日期，获取该客服"当日在线时长"。  备注：1、如果是操作者ID=被查者ID，返回被查者ID的"当日在线时长"。      2、如果操作者是组管理员，他可以查询他的组中的所有子帐号的"当日在线时长"。      3、如果操作者是主账户，他可以查询所有子帐号的"当日在线时长"。     4、被查者ID可以是多个，用 "," 隔开，id数不能超过30。     5、日累计在线时长定义：当日该用户累计的旺旺在线时长      6、开始时间与结束时间之间的间隔不能超过7天     7、不能查询90天以前的数据     8、不能查询当天的记录</SPAN>
# <UL>
# </UL>
class WangwangEserviceOnlinetimeGetRequest(object):
    def __init__(self):
        super(self.__class__, self).__init__()
        
        ## @brief <SPAN style="font-size:16px; font-family:'宋体','Times New Roman',Georgia,Serif;">获取API名称</SPAN>
        # <UL>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Type</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">str</SPAN>
        # </LI>
        # </UL>
        self.method = "taobao.wangwang.eservice.onlinetime.get"
        
        ## @brief <SPAN style="font-size:16px; font-family:'宋体','Times New Roman',Georgia,Serif;">时间戳，如果不设置,发送请求时将使用当时的时间</SPAN>
        # <UL>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Type</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">int</SPAN>
        # </LI>
        # </UL>
        self.timestamp = int(time.time())

        
        ## @brief <SPAN style="font-size:16px; font-family:'宋体','Times New Roman',Georgia,Serif;">结束日期</SPAN>
        # <UL>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Type</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">Date</SPAN>
        # </LI>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Required</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">required</SPAN>
        # </LI>
        # </UL>
        self.end_date = None
        
        ## @brief <SPAN style="font-size:16px; font-family:'宋体','Times New Roman',Georgia,Serif;">客服人员id：cntaobao+淘宝nick，例如cntaobaotest</SPAN>
        # <UL>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Type</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">String</SPAN>
        # </LI>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Required</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">required</SPAN>
        # </LI>
        # </UL>
        self.service_staff_id = None
        
        ## @brief <SPAN style="font-size:16px; font-family:'宋体','Times New Roman',Georgia,Serif;">开始日期</SPAN>
        # <UL>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Type</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">Date</SPAN>
        # </LI>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Required</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">required</SPAN>
        # </LI>
        # </UL>
        self.start_date = None
