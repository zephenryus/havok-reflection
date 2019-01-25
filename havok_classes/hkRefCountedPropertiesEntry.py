from .hkReferencedObject import hkReferencedObject
import struct


class hkRefCountedPropertiesEntry(object):
    object: any
    key: int
    flags: int

    def __init__(self, infile):
        self.object = any(infile)  # TYPE_POINTER:TYPE_STRUCT
        self.key = struct.unpack('>H', infile.read(2))  # TYPE_UINT16:TYPE_VOID
        self.flags = struct.unpack('>H', infile.read(2))  # TYPE_UINT16:TYPE_VOID

    def __repr__(self):
        return "<{class_name} object={object}, key={key}, flags={flags}>".format(**{
            "class_name": self.__class__.__name__,
            "object": self.object,
            "key": self.key,
            "flags": self.flags,
        })
