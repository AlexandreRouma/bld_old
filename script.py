import os
from command import *

class script(command):
    def __init__(self, name, interp, path, args = []):
        path = os.path.abspath(path)
        command.__init__(self, name, interp, [ path ] + args)