from .hkReferencedObject import hkReferencedObject
import struct
from .hkcdStaticTreeDefaultTreeStorage6 import hkcdStaticTreeDefaultTreeStorage6


class hkcdStaticAabbTree(hkReferencedObject):
    shouldDeleteTree: bool
    treePtr: any

    def __init__(self, infile):
        self.shouldDeleteTree = struct.unpack('>?', infile.read(1))  # TYPE_BOOL:TYPE_VOID
        self.treePtr = any(infile)  # TYPE_POINTER:TYPE_STRUCT

    def __repr__(self):
        return "<{class_name} shouldDeleteTree={shouldDeleteTree}, treePtr={treePtr}>".format(**{
            "class_name": self.__class__.__name__,
            "shouldDeleteTree": self.shouldDeleteTree,
            "treePtr": self.treePtr,
        })
