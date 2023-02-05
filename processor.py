import typing
import os
from program import *

import bldglobals

class processor:
    def __init__(self, prog:program, outGen:typing.Callable[[str],str], argGen:typing.Callable[[str, str, list],list]):
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
        relPath = os.path.dirname(os.path.relpath(input, bldglobals.TOP_LEVEL_DIR))
        outName = os.path.join(bldglobals.BUILD_DIR, os.path.join(relPath, self.__outGen(os.path.basename(input))))
        fargs = self.__argGen(input, outName, args)
        cmd = self.__prog.getPath()
        for a in fargs:
            cmd += ' ' + a
        return cmd, outName
