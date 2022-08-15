import os
import sys
import getopt

from processor import *
from program import *
from fileglob import *
from cexecutable import *

gcc = program('gcc')

src = globRecurse('test/src', '*.c')

test = c_executable(gcc, 'test', src, ['-O3'])

def dumpDep(tar:target, depth = 0):
    print('%sName: %s, File: %s, Commands: %s' % (' '*(depth * 4), tar.getName(), tar.getFile(), tar.getCommands()))
    for t in tar.getDepends():
        dumpDep(t, depth + 1)

dumpDep(test)