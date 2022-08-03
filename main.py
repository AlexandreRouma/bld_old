import os
import sys
import getopt

from processor import *
from program import *
from headerdepend import *
from fileglob import *

# cc = processor(gcc,
#     lambda inPath : inPath + '.o',
#     lambda inPath, outPath, args : [ '-o', outPath, '-c', inPath ] + args,
#     []
# )


print(globRecurse('test/src', '*.c'))