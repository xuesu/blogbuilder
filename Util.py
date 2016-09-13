__author__ = 'Administrator'
import os
import codecs

class Util:
    @staticmethod
    def fwriteb(desPath,srcPath):
        Util.checkDir(desPath)
        fout = open(desPath, "wb")
        fin = open(srcPath, "rb")
        fout.write(fin.read())
        fout.close()
        fin.close()

    @staticmethod
    def fwrite(desPath,content):
        Util.checkDir(desPath)
        fout = codecs.open(desPath, "w", "utf-8")
        fout.write(content)
        fout.close()

    @staticmethod
    def checkDir(desPath):
        desDir = ""
        for str in os.path.split(desPath)[:-1]:
            desDir = os.path.join(desDir, str)
            if not os.path.exists(desDir):
                os.makedirs(desDir)
            if not os.path.isdir(desDir):
                raise ValueError(desDir + ":The Directory is already a file!!")

    @staticmethod
    def readAll(srcPath):
        fin = codecs.open(srcPath,"r","utf-8")
        ans = fin.read()
        fin.close()
        return ans


    @staticmethod
    def readLines(srcPath):
        fin = codecs.open(srcPath,"r","utf-8")
        ans = fin.readlines()
        fin.close()
        return ans