from .hkReferencedObject import hkReferencedObject
import struct
from .hkRefCountedProperties import hkRefCountedProperties


class hkpBreakableMaterial(hkReferencedObject):
    strength: float
    typeAndFlags: int
    properties: hkRefCountedProperties

    def __init__(self, infile):
        self.strength = struct.unpack('>f', infile.read(4))
        self.typeAndFlags = struct.unpack('>i', infile.read(4))
        self.properties = hkRefCountedProperties(infile)  # TYPE_POINTER
