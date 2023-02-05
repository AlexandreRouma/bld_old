import os

class target:
    def __init__(self, name:str, file:str, commands:list, deps:list = [], includes:list = []):
        self.__name = name
        self.__file = os.path.abspath(file)
        self.__commands = commands
        self.__depends = deps
        self.__includes = includes

    def depends(self, dep:'target'):
        self.__depends.append(dep)

    def getName(self):
        return self.__name

    def getFile(self):
        return self.__file

    def getCommands(self):
        return self.__commands

    def getDepends(self):
        return self.__depends

    def getIncludes(self):
        return self.__includes