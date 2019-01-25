from .hkReferencedObject import hkReferencedObject
import struct
from .hkcdDynamicTreeDefaultTree48Storage import hkcdDynamicTreeDefaultTree48Storage


class hkcdDynamicAabbTree(hkReferencedObject):
    shouldDeleteTree: bool
    treePtr: hkcdDynamicTreeDefaultTree48Storage

    def __init__(self, infile):
        self.shouldDeleteTree = struct.unpack('>?', infile.read(1))
        self.treePtr = hkcdDynamicTreeDefaultTree48Storage(infile)  # TYPE_POINTER
