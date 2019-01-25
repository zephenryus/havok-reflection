from .hkcdDynamicTreeDynamicStoragePtr import hkcdDynamicTreeDynamicStoragePtr
import struct


class hkcdDynamicTreeTreehkcdDynamicTreeDynamicStoragePtr(hkcdDynamicTreeDynamicStoragePtr):
    numLeaves: int
    path: int
    root: int

    def __init__(self, infile):
        self.numLeaves = struct.unpack('>I', infile.read(4))
        self.path = struct.unpack('>I', infile.read(4))
        self.root = struct.unpack('>L', infile.read(8))
