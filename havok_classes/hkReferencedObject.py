from .hkBaseObject import hkBaseObject
import struct


class hkReferencedObject(hkBaseObject):
    memSizeAndRefCount: int

    def __init__(self, infile):
        self.memSizeAndRefCount = struct.unpack('>I', infile.read(4))  # TYPE_UINT32:TYPE_VOID

    def __repr__(self):
        return "<{class_name} memSizeAndRefCount={memSizeAndRefCount}>".format(**{
            "class_name": self.__class__.__name__,
            "memSizeAndRefCount": self.memSizeAndRefCount,
        })
