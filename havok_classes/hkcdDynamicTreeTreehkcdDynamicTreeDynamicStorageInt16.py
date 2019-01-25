from .hkcdDynamicTreeDynamicStorageInt16 import hkcdDynamicTreeDynamicStorageInt16
import struct


class hkcdDynamicTreeTreehkcdDynamicTreeDynamicStorageInt16(hkcdDynamicTreeDynamicStorageInt16):
    numLeaves: int
    path: int
    root: int

    def __init__(self, infile):
        self.numLeaves = struct.unpack('>I', infile.read(4))  # TYPE_UINT32:TYPE_VOID
        self.path = struct.unpack('>I', infile.read(4))  # TYPE_UINT32:TYPE_VOID
        self.root = struct.unpack('>I', infile.read(4))  # TYPE_UINT32:TYPE_VOID

    def __repr__(self):
        return "<{class_name} numLeaves={numLeaves}, path={path}, root={root}>".format(**{
            "class_name": self.__class__.__name__,
            "numLeaves": self.numLeaves,
            "path": self.path,
            "root": self.root,
        })
