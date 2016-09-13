__author__ = 'Administrator'
import os
import re
from Util import Util

class GenIndex:
    @staticmethod
    def getCateGory(dirInfo, fileInfo,param):
        if len(fileInfo) == 0:
            return ""
        if ":title" in fileInfo.keys():
            return "<li><a href = '%s'>%s</a></li>"% (re.sub('[\s]','_',(dirInfo)),  fileInfo[":title"])
        elif len(fileInfo.keys())>0:
            ans = ""
            ansleaf = []
            ansnode = []
            for (k,v) in fileInfo.items():
                subtitle = dirInfo + "/" + k
                subInfo = GenIndex.getCateGory(subtitle, v, param)
                if ":title" in v.keys():
                    ansnode.append(subInfo)
                else:
                    ansleaf.append(subInfo)
            ansleaf.sort()
            ansnode.sort()
            for str in ansleaf:
                ans = ans + str + os.linesep
            for str in ansnode:
                ans = ans + str + os.linesep
            t = ""
            if len(dirInfo) < 6:
                t = "CATEGORY"
            else:
                t = dirInfo[6:]
            return "<div id = '%s'>" % t + "<h2>%s</h2>" % t + "<ul>%s</ul>" % ans + "</div>"

    @staticmethod
    def getPureCateGory(dirInfo, fileInfo,param):
        if len(fileInfo) == 0:
            return ""
        if ":title" in fileInfo.keys():
            return ""
        elif len(fileInfo.keys())>0:
            ans = ""
            for (k,v) in fileInfo.items():
                if not ":title" in v.keys():
                    subtitle = dirInfo + "/" + k
                    subInfo = GenIndex.getCateGory(subtitle, v, param)
                    ans += os.linesep + subInfo
            #sub[sub.find("_sites")+7:]
            t = ""
            if len(dirInfo) < 6:
                t = "CATEGORY"
            else:
                t = dirInfo[6:]
            return "<div id = '%s'>" % t + "<h2>%s</h2>" % t + "<ul>%s</ul>" % ans + "</div>"

    @staticmethod
    def genIndex(desPath, fileInfo, param):
        defaultIndexTemplate = Util.readAll(param["defaultIndexPath"])

        category= GenIndex.getCateGory("/site", fileInfo, param)
        indexContent = re.sub(r"\{[\s]*\{[\s]*category[\s]*\}[\s]*\}", category, defaultIndexTemplate)
        #pureCategory = GenIndex.getCateGory("/site", fileInfo, param)
        #indexContent = re.sub(r"\{[\s]*\{[\s]*pureCategory[\s]*\}[\s]*\}", pureCategory, defaultIndexTemplate)
        Util.fwrite(desPath, indexContent)