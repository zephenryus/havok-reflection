from .hkReferencedObject import hkReferencedObject
import struct


class hclTransformSetDefinition(hkReferencedObject):
    name: str
    type: int
    numTransforms: int

    def __init__(self, infile):
        self.name = struct.unpack('>s', infile.read(0))
        self.type = struct.unpack('>i', infile.read(4))
        self.numTransforms = struct.unpack('>I', infile.read(4))
