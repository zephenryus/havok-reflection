from .hkcdDynamicTreeDynamicStorage16 import hkcdDynamicTreeDynamicStorage16
import struct


class hkcdDynamicTreeTreehkcdDynamicTreeDynamicStorage16(hkcdDynamicTreeDynamicStorage16):
    numLeaves: int
    path: int
    root: int

    def __init__(self, infile):
        self.numLeaves = struct.unpack('>I', infile.read(4))
        self.path = struct.unpack('>I', infile.read(4))
        self.root = struct.unpack('>H', infile.read(2))
