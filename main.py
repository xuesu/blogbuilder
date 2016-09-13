__author__ = 'xuesu'
from ConvertMd import ConvertMd
import codecs
import sys
import os
import shutil
import Util
import GenIndex

def init():
    pass

def execute():
    blogParam = dict()
    if len(sys.argv) == 3:
        blogParam["rootPath"] = sys.argv[2]
        blogParam["configPath"] = os.path.join(blogParam["rootPath"], "config.ini")
        blogParam["defaultPath"] = os.path.join(blogParam["rootPath"], "_layouts", "default.html")
        blogParam["defaultIndexPath"] = os.path.join(blogParam["rootPath"], "_layouts", "defaultIndex.html")
        blogParam["srcPath"] = os.path.join(blogParam["rootPath"], "_posts")
        blogParam["desPath"] = os.path.join(blogParam["rootPath"], "site")
        if os.path.exists(blogParam['desPath']):
            shutil.rmtree(blogParam['desPath'])
        fileInfo = ConvertMd.processFile(blogParam["srcPath"],
                                    blogParam["desPath"], blogParam)
        GenIndex.GenIndex.genIndex(os.path.join(blogParam["rootPath"],"index.html"), fileInfo, blogParam)
    else:
        raise IOError("arguments error,you should type python main.py execute <your blog root path>")

if __name__ == '__main__':
    if sys.argv[1] == 'install':
        init()
    elif sys.argv[1] == 'execute':
        execute()

