__author__ = 'Administrator'
import os
import re
from Util import Util

class GenIndex:
    def getCateGory(dirInfo, fileInfo,param):
        if len(fileInfo) == 0:
            return ""
        if ":title" in fileInfo.keys():
            return "<li><a href = '%s'>%s</a></li>"% (re.sub('[\s]','_',(dirInfo)),  fileInfo[":title"])
        elif len(fileInfo.keys())>0:
            ans = ""
            for (k,v) in fileInfo.items():
                subtitle = dirInfo + "/" + k
                subInfo = GenIndex.getCateGory(subtitle, v, param)
                ans += os.linesep + subInfo
            #sub[sub.find("_sites")+7:]
            t = ""
            if len(dirInfo) < 6:
                t = "CATEGORY"
            else:
                t = dirInfo[6:]
            return "<h2>%s</h2>" % t + "<ul>%s</ul>"% ans

    def genIndex(desPath, fileInfo, param):
        defaultIndexTemplate = Util.readAll(param["defaultIndexPath"])
        category= GenIndex.getCateGory("/site", fileInfo, param)
        indexContent = re.sub(r"\{[\s]*\{[\s]*category[\s]*\}[\s]*\}", category, defaultIndexTemplate)
        Util.fwrite(desPath, indexContent)