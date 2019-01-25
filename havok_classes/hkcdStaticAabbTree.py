from .hkReferencedObject import hkReferencedObject
import struct
from .hkcdStaticTreeDefaultTreeStorage6 import hkcdStaticTreeDefaultTreeStorage6


class hkcdStaticAabbTree(hkReferencedObject):
    shouldDeleteTree: bool
    treePtr: hkcdStaticTreeDefaultTreeStorage6

    def __init__(self, infile):
        self.shouldDeleteTree = struct.unpack('>?', infile.read(1))
        self.treePtr = hkcdStaticTreeDefaultTreeStorage6(infile)  # TYPE_POINTER
