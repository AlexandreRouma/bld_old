#!/usr/bin/python
import os
import sys
import getopt

from generator import *
from program import *

def exec_abs(__build_file_source):
    exec(__build_file_source)

def include_subdirectory(path):
    # Save working directory
    cwd = os.getcwd()

    # Read the source
    file = open(path + '/build.bld')
    src = file.read()
    file.close()

    # chdir to match file
    os.chdir(path)

    # Execute
    exec_abs(src)

    # Switch back to original working directory
    os.chdir(cwd)

include_subdirectory(sys.argv[1])