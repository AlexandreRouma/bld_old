from target import *

class command(target):
    def __init__(self, name, prog, args, depends = []):
        argStr = ''
        for a in args:
            argStr += a + ' '
        argStr = argStr.strip()

        target.__init__(self, name, '', [
            '%s %s' % (prog.getPath(), argStr)
        ], depends)