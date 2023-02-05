import os
from target import *

class source(target):
    def __init__(self, path):
        path = os.path.abspath(path)
        target.__init__(self, path, path, [])