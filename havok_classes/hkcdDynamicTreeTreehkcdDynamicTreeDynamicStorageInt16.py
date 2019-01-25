from .hkcdDynamicTreeDynamicStorageInt16 import hkcdDynamicTreeDynamicStorageInt16
import struct


class hkcdDynamicTreeTreehkcdDynamicTreeDynamicStorageInt16(hkcdDynamicTreeDynamicStorageInt16):
    numLeaves: int
    path: int
    root: int

    def __init__(self, infile):
        self.numLeaves = struct.unpack('>I', infile.read(4))
        self.path = struct.unpack('>I', infile.read(4))
        self.root = struct.unpack('>I', infile.read(4))
