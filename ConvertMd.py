__author__ = 'xuesu'
import markdown
import os
import codecs
import re
import markdown.extensions.toc
from Util import Util

class ConvertMd:
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
                    if fileName.endswith(".md"):
                        desFileName = fileName[:fileName.rfind(".")] + ".html"
                        subRes = ConvertMd.processFile(os.path.join(srcPath, fileName), os.path.join(desPath, desFileName),param)
                        d[desFileName] = subRes
                    else:
                        subRes = ConvertMd.processFile(os.path.join(srcPath, fileName), os.path.join(desPath, fileName),param)
                        d[fileName] = subRes
                return d
            if os.path.isfile(srcPath):
                if not srcPath.endswith(".md"):
                    Util.fwriteb(re.sub('[\s]','_',desPath), srcPath)
                    return {":title":os.path.split(srcPath)[-1]}
                else:
                    fin = codecs.open(srcPath, "r", "utf-8")
                    content = fin.read()
                    fin.close()
                    md = markdown.Markdown(extensions=[markdown.extensions.toc.TocExtension(baselevel=1)],
                                           output_format="html")
                    html = md.convert(content)
                    #print(html)
                    defaultHtml = Util.readAll(param["defaultPath"])
                    htmlContent = re.sub(r"\{[\s]*\{[\s]*content[\s]*\}[\s]*\}", html, defaultHtml)
                    #print(htmlContent)
                    title = os.path.split(srcPath)[-1][:srcPath.rfind(".")][:-3]
                    titleContent = re.sub(r"\{[\s]*\{[\s]*title[\s]*\}[\s]*\}", title, htmlContent)
                    Util.fwrite(re.sub('[\s]','_',desPath), titleContent)
                    return {":title":title}
