from .hkBaseObject import hkBaseObject
import struct


class hkReferencedObject(hkBaseObject):
    memSizeAndRefCount: int

    def __init__(self, infile):
        self.memSizeAndRefCount = struct.unpack('>I', infile.read(4))
