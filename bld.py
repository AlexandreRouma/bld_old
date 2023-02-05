#!/usr/bin/python3
import os
import sys

import bldglobals
bldglobals.TOP_LEVEL_DIR = os.path.abspath(sys.argv[1])
bldglobals.BUILD_DIR = os.getcwd()

from processor import *
from program import *
from fileglob import *
from c_executable import *
from makegen import *
from command import *
from source import *

def exec_abs(__build_file_source, args):
    # Define variables
    for k in args:
        locals()[k] = args[k]

    # Call build code
    exec(__build_file_source)

def include_subdirectory(path, args = {}):
    # Save working directory
    cwd = os.getcwd()

    # Read the source
    file = open(path + '/build.bld')
    src = file.read()
    file.close()

    # chdir to match file
    os.chdir(path)

    # Execute
    exec_abs(src, args)

    # Switch back to original working directory
    os.chdir(cwd)

include_subdirectory(bldglobals.TOP_LEVEL_DIR, { 'OPT_ARG_LMAO': 'test' })