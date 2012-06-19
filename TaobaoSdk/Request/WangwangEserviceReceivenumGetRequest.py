#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim: set ts=4 sts=4 sw=4 et:


## @brief 根据操作者ID，返回被查者ID指定时间段内每个帐号的"已接待人数"<br/> 备注：<br/> 1、如果是操作者ID=被查者ID，返回被查者ID的"已接待人数"。<br/> 2、如果操作者是组管理员，他可以查询他的组中的所有子帐号的"已接待人数"。<br/> 3、如果操作者是主账户，他可以查询所有子帐号的"已接待人数"。<br/> （注意：这里说的是授权是主帐号，可以查询所有子帐号的数据，具体要查询哪些子账号的数据，需要在service_staff_id具体指定，而不是service_staff_id直接输入主帐号）<br/>  4、被查者ID可以是多个，用 "," 隔开，id数不能超过30。<br/>  5、规则：某客服在1天内和同一个客户交流了多次，已回复人数算1。<br/> 6、"已接待人数"定义：买家、卖家彼此发过至少1条消息 ，不论谁先发都可以。<br/>   7、被查者ID可以是多个，用 "," 隔开，id数不能超过30。<br/>   8、开始时间与结束时间之间的间隔不能超过7天<br/>   9、不能查询90天以前的数据<br/>   10、不能查询当天的记录<br/>    11、查询日期精确到日<br/>
# @author wuliang@maimiaotech.com
# @date 2012-06-19 10:43:34
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


## @brief <SPAN style="font-size:16px; font-family:'宋体','Times New Roman',Georgia,Serif;">根据操作者ID，返回被查者ID指定时间段内每个帐号的"已接待人数"<br/> 备注：<br/> 1、如果是操作者ID=被查者ID，返回被查者ID的"已接待人数"。<br/> 2、如果操作者是组管理员，他可以查询他的组中的所有子帐号的"已接待人数"。<br/> 3、如果操作者是主账户，他可以查询所有子帐号的"已接待人数"。<br/> （注意：这里说的是授权是主帐号，可以查询所有子帐号的数据，具体要查询哪些子账号的数据，需要在service_staff_id具体指定，而不是service_staff_id直接输入主帐号）<br/>  4、被查者ID可以是多个，用 "," 隔开，id数不能超过30。<br/>  5、规则：某客服在1天内和同一个客户交流了多次，已回复人数算1。<br/> 6、"已接待人数"定义：买家、卖家彼此发过至少1条消息 ，不论谁先发都可以。<br/>   7、被查者ID可以是多个，用 "," 隔开，id数不能超过30。<br/>   8、开始时间与结束时间之间的间隔不能超过7天<br/>   9、不能查询90天以前的数据<br/>   10、不能查询当天的记录<br/>    11、查询日期精确到日<br/></SPAN>
# <UL>
# </UL>
class WangwangEserviceReceivenumGetRequest(object):
    def __init__(self):
        super(self.__class__, self).__init__()
        
        ## @brief <SPAN style="font-size:16px; font-family:'宋体','Times New Roman',Georgia,Serif;">获取API名称</SPAN>
        # <UL>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Type</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">str</SPAN>
        # </LI>
        # </UL>
        self.method = "taobao.wangwang.eservice.receivenum.get"
        
        ## @brief <SPAN style="font-size:16px; font-family:'宋体','Times New Roman',Georgia,Serif;">时间戳，如果不设置,发送请求时将使用当时的时间</SPAN>
        # <UL>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Type</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">int</SPAN>
        # </LI>
        # </UL>
        self.timestamp = int(time.time())

        
        ## @brief <SPAN style="font-size:16px; font-family:'宋体','Times New Roman',Georgia,Serif;">查询接待人数的结束日期 时间精确到日 时分秒可以直接传00:00:00</SPAN>
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
        
        ## @brief <SPAN style="font-size:16px; font-family:'宋体','Times New Roman',Georgia,Serif;">查询接待人数的开始日期 时间精确到日 时分秒可直接传 00:00:00</SPAN>
        # <UL>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Type</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">Date</SPAN>
        # </LI>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Required</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">required</SPAN>
        # </LI>
        # </UL>
        self.start_date = None
