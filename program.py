import subprocess

class program:
    def __init__(self, name):
        self.__name = name
        res = subprocess.run(['which', name], stdout=subprocess.PIPE)
        self.__path = res.stdout.decode('utf8').strip()

    def getName(self):
        return self.__name

    def getPath(self):
        return self.__path
    
    __name = ''
    __path = ''