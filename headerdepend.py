import subprocess
import os

def getHeaders(compiler, cxxPath):
    if not compiler.getName().endswith('gcc'):
        raise Exception('Unsupported compiler')

    headers = []
    res = subprocess.run(['gcc', '-MM', cxxPath, '-o', '-'], stdout=subprocess.PIPE)
    makeline = res.stdout.decode('utf8').strip()
    _headers = makeline.split(':')[1].split(' ')[2:]

    for h in _headers:
        hc = h.strip()
        if hc == '':
            continue
        headers.append(os.path.abspath(hc))

    return headers