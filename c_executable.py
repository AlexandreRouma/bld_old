from target import *
from source import *
from processor import *

import bldglobals

class c_executable(target):
    def __init__(self, name:str, sources:list, cArgs:list = [], cxxArgs:list = [], asmArgs:list = [], linkArgs:list = [], cc = None, cxx = None, asm = None, cl = None):
        # Save parameters
        self.__name = name
        self.__cArgs = cArgs
        self.__cxxArgs = cxxArgs
        self.__asmArgs = asmArgs
        self.__linkArgs = linkArgs
        self.__c_sources = []
        self.__cxx_sources = []
        self.__asm_sources = []
        self.__cc = None
        self.__cxx = None
        self.__asm = None
        self.__cl = None
        
        # Sort sources
        for s in sources:
            ext = os.path.splitext(s)[1]
            if ext == '.c':
                self.__c_sources += [s]
            elif ext == '.cpp' or ext == '.cxx' or ext == '.c++':
                self.__cxx_sources += [s]
            elif ext == '.s' or ext == '.as' or ext == '.asm':
                self.__asm_sources += [s]
        
        # Save C compîler
        if cc != None:
            self.__cc = cc 
        else:
            self.__cc = cxx

        # Save CXX compiler
        self.__cxx = cxx

        # Save ASM assembler
        self.__asm = asm

        # Save linker
        if cl != None:
            self.__cl = cl 
        elif cc != None:
            self.__cl = cc
        elif cxx != None:
            self.__cl = cxx

        # Generate targets
        self.__generate()
    
    def __generate(self):
        # Reset dependencies and includes
        self._target__depends = []
        self._target__includes = []

        cObjsFiles = []
        cxxObjsFiles = []
        asmObjsFiles = []

        if self.__cc != None:
            # Create C Makedep processor
            c_md_proc = processor(self.__cc,
                lambda inName : inName + '.makedep',
                lambda inPath, outPath, args : args + [ '-MM', inPath, '>', outPath ]
            )
        
            # Create C compiler processor
            c_proc = processor(self.__cc,
                lambda inName : inName + '.o',
                lambda inPath, outPath, args : args + [ '-o', outPath, '-c', inPath ]
            )

            # Generate C targets
            cObjs = c_proc(self.__c_sources, self.__cArgs)
            cObjsFiles = []
            for i in range(0, len(cObjs)):
                o = cObjs[i]
                m = c_md_proc(self.__c_sources[i], self.__cArgs + [ '-MT', o[1] ])
                s = self.__c_sources[i]
                cObjsFiles += [o[1]]
                self.depends(target(o[1], o[1], [ m[0], o[0] ], [ source(s) ], [m[1]]))

        if self.__cxx != None:
            # Create C++ Makedep processor
            cxx_md_proc = processor(self.__cxx,
                lambda inName : inName + '.makedep',
                lambda inPath, outPath, args : args + [ '-MM', inPath, '>', outPath ]
            )
            
            # Create C++ compiler processor
            cxx_proc = processor(self.__cxx,
                lambda inName : inName + '.o',
                lambda inPath, outPath, args : args + [ '-o', outPath, '-c', inPath ]
            )

            # Generate C++ targets
            cxxObjs = cxx_proc(self.__cxx_sources, self.__cxxArgs)
            cxxObjsFiles = []
            for i in range(0, len(cxxObjs)):
                o = cxxObjs[i]
                m = c_md_proc(self.__cxx_sources[i], self.__cxxArgs + [ '-MT', o[1] ])
                s = self.__cxx_sources[i]
                cxxObjsFiles += [o[1]]
                self.depends(target(o[1], o[1], [ m[0], o[0] ], [ source(s) ], [m[1]]))
        
        if self.__asm != None:
            # Create Assembler processor
            asm_proc = processor(self.__asm,
                lambda inName : inName + '.o',
                lambda inPath, outPath, args : args + [ '-o', outPath, inPath ]
            )

            # Generate ASM targets
            asmObjs = asm_proc(self.__asm_sources, self.__asmArgs)
            asmObjsFiles = []
            for i in range(0, len(asmObjs)):
                o = asmObjs[i]
                s = self.__asm_sources[i]
                asmObjsFiles += [o[1]]
                self.depends(target(o[1], o[1], [ o[0] ], [ source(s) ]))


        # Combine all objects
        objs = cObjsFiles + cxxObjsFiles + asmObjsFiles
        objStr = ''
        for o in objs:
            objStr += o + ' '
        objStr = objStr.strip()

        # Generate linker argument string
        clArgs = ''
        for a in self.__linkArgs:
            clArgs += a + ' '

        # Set main target
        self._target__name = self.__name
        self._target__file = os.path.join(bldglobals.BUILD_DIR, self.__name)
        self._target__commands = [
            '%s %s -o %s %s' % (self.__cl.getPath(), clArgs, self._target__file, objStr)
        ]