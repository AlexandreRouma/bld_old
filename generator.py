import typing
import os
from program import *

class generator:
    def __init__(self, prog:program, outGen:typing.Callable[[str],str], argGen:typing.Callable[[str, str, list],list], args:list):
        self.__prog = prog
        self.__outGen = outGen
        self.__argGen = argGen
        self.__args = args

    def __call__(self, input):
        # Batch process if needed
        if type(input) == list:
            outputs = []
            for f in input:
                outputs.append(self(f))
            return outputs
        
        # Generate the data
        outName = self.__outGen(os.path.basename(input))
        args = self.__argGen(input, outName, self.__args)
        cmd = self.__prog.getPath()
        for a in args:
            cmd += ' ' + a
        return cmd, outName
