from target import *
from processor import *

class c_executable(target):
    def __init__(self, compiler:program, name:str, sources:list, compArgs:list = [], linkArgs:list = [], linker = None):
        self.__compiler = compiler
        if linker != None:
            self.__linker = linker
        else:
            self.__linker = compiler
        self.__sources = sources
        self.__compArgs = compArgs
        self.__linkArgs = linkArgs
        
        # Create compiler processor
        self.__cc = processor(compiler,
            lambda inPath : inPath + '.o',
            lambda inPath, outPath, args : args + [ '-o', outPath, '-c', inPath ]
        )

        # Init target
        target.__init__(self, name, name, '')

        self.__update()

    def __update(self):
        # Generate object targets
        objs = self.__cc(self.__sources, self.__compArgs)
        objStr = ''
        for i in range(0, len(objs)):
            o = objs[i]
            s = self.__sources[i]
            objStr += o[1] + ' '
            self.depends(target(o[1], o[1], [o[0]], [target(s, s, [], [])]))

        # Generate linker target
        argsStr = ''
        for a in self.__linkArgs:
            argsStr += a + ' '
        objStr = objStr.strip()
        argsStr = argsStr.strip()
        self._target__commands = ['%s %s -o %s %s' % (self.__linker.getPath(), argsStr, self._target__name, objStr)]

    __compiler = None
    __linker = None
    __cc = None
    __sources = []
    __compArgs = []
    __linkArgs = []