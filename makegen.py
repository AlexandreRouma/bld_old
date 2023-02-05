import os
from target import *
import bldglobals

def makegen(target:target, path:str):
    file = open(path, 'w')

    __writeDep(file, target)

    file.write('.PHONY: clean\n')
    file.write('clean:\n')
    file.write('\t@find %s ! -name \'Makefile\' -type f -exec rm -f {} +\n' % (bldglobals.BUILD_DIR))
    file.write('\t@echo Removed build files.\n')

def __writeDep(file, tar:target, depth = 0):
    if len(tar.getCommands()) > 0 or len(tar.getDepends()):
        depStr = ''
        for d in tar.getDepends():
            if d.getFile() != '':
                depStr += d.getFile() + ' '
            else:
                depStr += d.getName() + ' '
        depStr = depStr.strip()

        for i in tar.getIncludes():
            file.write('-include %s\n' % (i))

        if tar.getFile() == '':
            file.write('%s: %s\n' % (tar.getName(), depStr))
            file.write('\t@echo %s\n' % (tar.getName()))
        else:
            file.write('%s: %s\n' % (tar.getFile(), depStr))
            file.write('\t@echo %s\n' % (tar.getName()))
            file.write('\t@mkdir -p %s\n' % (os.path.dirname(tar.getFile())))

        for c in tar.getCommands():
            file.write('\t@%s\n' % (c))

        file.write('\n')

    for t in tar.getDepends():
        __writeDep(file, t, depth + 1)

