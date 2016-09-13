__author__ = 'xuesu'
import markdown
import os
import codecs
import re
import markdown.extensions.toc
from Util import Util

class ConvertMd:
    @staticmethod
    def processFile(srcPath, desPath, param):
        '''
        :param srcPath sourceFile Path,it can only solve utf-8 .md now:
        :param desPath: destFile Path
        :param defaultHtml: Template Model, details Page Html
        '''
        print("processFile:des:"+desPath + " src:"+srcPath)
        if os.path.exists(srcPath):
            if os.path.isdir(srcPath):
                d = dict()
                for fileName in os.listdir(srcPath):
                    if not isinstance(fileName,unicode):
                        fileName = unicode(fileName,"utf-8")
                    if fileName.endswith(u".md"):
                        desFileName = fileName[:fileName.rfind(u".")] + u".html"
                        subRes = ConvertMd.processFile(os.path.join(srcPath, fileName), os.path.join(desPath, desFileName),param)
                        d[desFileName] = subRes
                    else:
                        subRes = ConvertMd.processFile(os.path.join(srcPath, fileName), os.path.join(desPath, fileName),param)
                        d[fileName] = subRes
                return d
            if os.path.isfile(srcPath):
                if not srcPath.endswith(u".md"):
                    Util.fwriteb(re.sub(u'[\s]',u'_',desPath), srcPath)
                    return {u":title":os.path.split(srcPath)[-1]}
                else:
                    fin = codecs.open(srcPath, "r", "utf-8")
                    content = fin.read()
                    fin.close()
                    
                    md = markdown.Markdown(extensions=[markdown.extensions.toc.TocExtension(baselevel=1),"fenced_code","tables"],
                                           output_format="html")
                    html = md.convert(content)
                    html = ur'%s' % html
                    #print(html)
                    defaultHtml = Util.readAll(param["defaultPath"])
                    #print(defaultHtml)
                    htmlContent = re.sub(ur"{[\s]*{[\s]*content[\s]*}[\s]*}", html, defaultHtml)
                    #print(htmlContent)
                    title = os.path.split(srcPath)[-1][:srcPath.rfind(".")][:-3]
                    if not isinstance(title,unicode):
                        title = unicode(title,"utf-8")
                    titleContent = re.sub(ur"{[\s]*{[\s]*title[\s]*}[\s]*}", title, htmlContent)
                    Util.fwrite(re.sub(u'[\s]',u'_',desPath), titleContent)
                    return {":title":title}
