#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim: set ts=4 sts=4 sw=4 et:
"""
@author: Wu Liang
@authors: 
@date: 9:13:07 PM Jun 5, 2012
@contact: wuliang@maimiaotech.com 
@version: 0.0.0
@deprecated:
@license:
@copyright:
"""

from Common import *
from Settings import *

class ResponseParser(object):
    def __init__(self, root, output):
        self.root = root
        self.output = output
        
    def generateFiles(self):
        rootOutput = os.path.join(self.output, responseOutput)
        if not os.path.exists(rootOutput):
            os.makedirs(rootOutput)
        imported = set()
        for api in self.root.getElementsByTagName("api"):
            name = api.getElementsByTagName("name")[0].firstChild.data
            name = name.encode("utf-8")
            name = str().join([x.capitalize() for x in name.lstrip("taobao").split(".") if x != str()])
            name += "Response"
            imported.add(name)
            filename = os.path.join(rootOutput, name + ".py")
            print "Generating %s" % (filename)
            templateFile = Template(file(responseTemplate).read().decode("utf-8"))
            rendered = templateFile.render_unicode(api=api).encode("utf-8")
            rendered = rendered.replace("\\#\\#", "##")
            fout = file(filename, "w")
            fout.write(rendered)
            fout.close()
        #imported.add("ErrorResponse")
        templateFile = Template(file(initTemplate).read().decode("utf-8"))
        rendered = templateFile.render_unicode(imports=imported).encode("utf-8")
        fout = file(os.path.join(rootOutput, "__init__.py"), "w")
        fout.write(rendered)
        fout.close()
            
            
