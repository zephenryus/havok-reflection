from .hkReferencedObject import hkReferencedObject
import struct
from .hkRefCountedProperties import hkRefCountedProperties


class hkpBreakableMaterial(hkReferencedObject):
    strength: float
    typeAndFlags: int
    properties: any

    def __init__(self, infile):
        self.strength = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.typeAndFlags = struct.unpack('>i', infile.read(4))  # TYPE_INT32:TYPE_VOID
        self.properties = any(infile)  # TYPE_POINTER:TYPE_STRUCT

    def __repr__(self):
        return "<{class_name} strength={strength}, typeAndFlags={typeAndFlags}, properties={properties}>".format(**{
            "class_name": self.__class__.__name__,
            "strength": self.strength,
            "typeAndFlags": self.typeAndFlags,
            "properties": self.properties,
        })
