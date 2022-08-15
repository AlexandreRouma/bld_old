import typing
import os
from program import *

class processor:
    def __init__(self, prog:program, outGen:typing.Callable[[str],str], argGen:typing.Callable[[str, str, list],list], root = None):
        self.__prog = prog
        self.__outGen = outGen
        self.__argGen = argGen

    def __call__(self, input, args):
        # Batch process if needed
        if type(input) == list:
            outputs = []
            for f in input:
                outputs.append(self(f, args))
            return outputs
        
        # Generate the data
        input = os.path.abspath(input)
        outName = self.__outGen(os.path.basename(input))
        fargs = self.__argGen(input, outName, args)
        cmd = self.__prog.getPath()
        for a in fargs:
            cmd += ' ' + a
        return cmd, outName
