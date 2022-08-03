import fnmatch
import os

def glob(path, pattern):
    result = []
    fns = os.listdir(path)
    for fn in fns:
        if fnmatch.fnmatch(fn, pattern):
            result.append(os.path.join(path, fn))
    return result

def globRecurse(path, pattern):
    result = []
    walks = os.walk(path)
    for root, __, fns in walks:
        for fn in fns:
            if fnmatch.fnmatch(fn, pattern):
                result.append(os.path.join(root, fn))
    return result