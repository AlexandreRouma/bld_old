import subprocess
import shutil

class program:
    def __init__(self, name):
        self.__name = name
        self.__path = shutil.which(name)

    def getName(self):
        return self.__name

    def getPath(self):
        return self.__path
    
    __name = ''
    __path = ''