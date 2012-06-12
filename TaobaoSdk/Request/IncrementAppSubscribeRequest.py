#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim: set ts=4 sts=4 sw=4 et:



## @brief 此接口用于ISV订阅增量消息。  只有开通了增量消息角色的ISV才能开通增量消息的服务  如果ISV已经开通了增量消息服务，重复开通会跟据传入的参数更新ISV的服务记录（如：订阅字段、有效期限等等）  传入的topics消息类型的数量和顺序要和传入的status消息状态所属的类型的数量和顺序要一致。传了某个消息类型的topic却传入他对应位置的status为""(空字符串)时表示订阅这个topic下的所有消息  每次订阅操作如果是更新旧有数据，那么会进行替换操作，即：会使用当前传入要更新的数据置换久的数据，而不会执行合并的操作。例如：以前订阅了trade的所有消息，这次更新的时候传入了topic为refund，status为RefundSuccess。那么此时用户不是既定阅了交易所有的消息又定了退款成功的消息，而是只订阅了退款成功的消息。
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
from Response import IncrementAppSubscribeResponse


## @brief <SPAN style="font-size:16px; font-family:'宋体','Times New Roman',Georgia,Serif;">此接口用于ISV订阅增量消息。  只有开通了增量消息角色的ISV才能开通增量消息的服务  如果ISV已经开通了增量消息服务，重复开通会跟据传入的参数更新ISV的服务记录（如：订阅字段、有效期限等等）  传入的topics消息类型的数量和顺序要和传入的status消息状态所属的类型的数量和顺序要一致。传了某个消息类型的topic却传入他对应位置的status为""(空字符串)时表示订阅这个topic下的所有消息  每次订阅操作如果是更新旧有数据，那么会进行替换操作，即：会使用当前传入要更新的数据置换久的数据，而不会执行合并的操作。例如：以前订阅了trade的所有消息，这次更新的时候传入了topic为refund，status为RefundSuccess。那么此时用户不是既定阅了交易所有的消息又定了退款成功的消息，而是只订阅了退款成功的消息。</SPAN>
# <UL>
# <LI>
# <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">CName</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">ISV订阅增量消息</SPAN>
# </LI>
# <LI>
# <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Authorize</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">不需用户授权</SPAN>
# </LI>
# </UL>
class IncrementAppSubscribeRequest(object):
    def __init__(self):
        super(self.__class__, self).__init__()
        
        ## @brief <SPAN style="font-size:16px; font-family:'宋体','Times New Roman',Georgia,Serif;">获取API名称</SPAN>
        # <UL>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Type</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">str</SPAN>
        # </LI>
        # </UL>
        self.method = "taobao.increment.app.subscribe"
        
        ## @brief <SPAN style="font-size:16px; font-family:'宋体','Times New Roman',Georgia,Serif;">时间戳，如果不设置,发送请求时将使用当时的时间</SPAN>
        # <UL>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Type</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">int</SPAN>
        # </LI>
        # </UL>
        self.timestamp = int(time.time())

        
        ## @brief <SPAN style="font-size:16px; font-family:'宋体','Times New Roman',Georgia,Serif;">要订阅的消息类别。可多个类别同时订阅，每种类型之间以";"分隔。具体选值请见：增量消息类型说明。例如，如果要同时订阅交易，退款，商品的消息传入的字符串就是"trade;refund;item"</SPAN>
        # <UL>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Type</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">String</SPAN>
        # </LI>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Level</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">Basic</SPAN>
        # </LI>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Required</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">必须</SPAN>
        # </LI>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Sample</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">trade;refund;item</SPAN>
        # </LI>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Default</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">None</SPAN>
        # </LI>
        # </UL>
        self.topics = None
        
        ## @brief <SPAN style="font-size:16px; font-family:'宋体','Times New Roman',Georgia,Serif;">要订阅的消息状态。可选值有：商品消息状态、退款消息状态、交易消息状态里面的状态类型。status字段支持多个状态同时订阅。每个大类的状态（商品消息状态里的所有消息状态属于同一个大类，退款消息状态里的所有消息状态属于同一个大类，交易消息状态里的所有消息状态属于同一个大类）要合并到一起传入。每个大类的消息内部用","连接，大类之间用";"连接。另，大类的排列顺序要和topics入参中类型的顺序一一对应，如果不传具体某个大类的消息而传入all，表示订阅这个大类下所有的消息状态。如：传入了topics="trade;refund;item"时：当传入status="all;all;all"表示我订阅者三种类型消息下的所有状态的消息；当传入status="TradeCreate,TradeSuccess;all;ItemDelete"表示我订阅交易类型下的交易创建和交易成功的消息，退款类型下的所有退款相关消息，商品下的商品删除的消息。</SPAN>
        # <UL>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Type</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">String</SPAN>
        # </LI>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Level</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">Basic</SPAN>
        # </LI>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Required</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">必须</SPAN>
        # </LI>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Sample</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">TradeCreate,TradeSuccess;all;ItemDelete</SPAN>
        # </LI>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Default</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">None</SPAN>
        # </LI>
        # </UL>
        self.status = None
        
        ## @brief <SPAN style="font-size:16px; font-family:'宋体','Times New Roman',Georgia,Serif;">ISV订阅服务时间，以月计算。目前可选值：1、3、6、12四种时间间隔。如果ISV属于淘宝的合作伙伴或者是自用型，可以选择订阅时间为-1（表示永久订阅）</SPAN>
        # <UL>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Type</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">Number</SPAN>
        # </LI>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Level</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">Basic</SPAN>
        # </LI>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Required</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">必须</SPAN>
        # </LI>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Sample</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">1</SPAN>
        # </LI>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Default</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">None</SPAN>
        # </LI>
        # </UL>
        self.duration = None
