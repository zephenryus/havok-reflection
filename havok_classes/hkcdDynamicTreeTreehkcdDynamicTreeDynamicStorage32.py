from .hkcdDynamicTreeDynamicStorage32 import hkcdDynamicTreeDynamicStorage32
import struct


class hkcdDynamicTreeTreehkcdDynamicTreeDynamicStorage32(hkcdDynamicTreeDynamicStorage32):
    numLeaves: int
    path: int
    root: int

    def __init__(self, infile):
        self.numLeaves = struct.unpack('>I', infile.read(4))
        self.path = struct.unpack('>I', infile.read(4))
        self.root = struct.unpack('>I', infile.read(4))
