from .hkReferencedObject import hkReferencedObject
import struct


class hclTransformSetDefinition(hkReferencedObject):
    name: str
    type: int
    numTransforms: int

    def __init__(self, infile):
        self.name = struct.unpack('>s', infile.read(0))  # TYPE_STRINGPTR:TYPE_VOID
        self.type = struct.unpack('>i', infile.read(4))  # TYPE_INT32:TYPE_VOID
        self.numTransforms = struct.unpack('>I', infile.read(4))  # TYPE_UINT32:TYPE_VOID

    def __repr__(self):
        return "<{class_name} name=\"{name}\", type={type}, numTransforms={numTransforms}>".format(**{
            "class_name": self.__class__.__name__,
            "name": self.name,
            "type": self.type,
            "numTransforms": self.numTransforms,
        })
