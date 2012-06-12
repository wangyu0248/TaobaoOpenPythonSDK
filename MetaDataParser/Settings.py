#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim: set ts=4 sts=4 sw=4 et:
"""
@author: Wu Liang
@authors: 
@date: 11:49:01 PM Jun 4, 2012
@contact: wuliang@maimiaotech.com 
@version: 0.0.0
@deprecated:
@license:
@copyright:
"""

import os

def __getCurrentPath():
    return os.path.normpath(os.path.join(os.path.realpath(__file__), os.path.pardir))

# 模板文件的路径
pyTemplatePath = os.path.join(__getCurrentPath(), "templates")

# domain的模板
domainTemplate = os.path.join(pyTemplatePath, "domain.template")
domainOutput = "Domain"

# __init__.py的模板
initTemplate = os.path.join(pyTemplatePath, "init.template")

# request的模板
requestTemplate = os.path.join(pyTemplatePath, 'request.template')
requestOutput = "Request"

# response的模板
responseTemplate = os.path.join(pyTemplatePath, 'response.template')
responseOutput = "Response"

# sdkCommon的模版
sdkCommonTemplate = os.path.join(pyTemplatePath, "SdkCommon.template")
sdkCommonOutput = "SdkCommon.py"

# 错误Response
errorResponseTemplate = os.path.join(pyTemplatePath, "ErrorResponse.py")
errorResponseOutput = "ErrorResponse.py"