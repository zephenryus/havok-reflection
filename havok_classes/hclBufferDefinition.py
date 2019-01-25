from .hkReferencedObject import hkReferencedObject
import struct
from .hclBufferLayout import hclBufferLayout


class hclBufferDefinition(hkReferencedObject):
    name: str
    type: int
    subType: int
    numVertices: int
    numTriangles: int
    bufferLayout: hclBufferLayout

    def __init__(self, infile):
        self.name = struct.unpack('>s', infile.read(0))  # TYPE_STRINGPTR:TYPE_VOID
        self.type = struct.unpack('>i', infile.read(4))  # TYPE_INT32:TYPE_VOID
        self.subType = struct.unpack('>i', infile.read(4))  # TYPE_INT32:TYPE_VOID
        self.numVertices = struct.unpack('>I', infile.read(4))  # TYPE_UINT32:TYPE_VOID
        self.numTriangles = struct.unpack('>I', infile.read(4))  # TYPE_UINT32:TYPE_VOID
        self.bufferLayout = hclBufferLayout(infile)  # TYPE_STRUCT:TYPE_VOID

    def __repr__(self):
        return "<{class_name} name=\"{name}\", type={type}, subType={subType}, numVertices={numVertices}, numTriangles={numTriangles}, bufferLayout={bufferLayout}>".format(**{
            "class_name": self.__class__.__name__,
            "name": self.name,
            "type": self.type,
            "subType": self.subType,
            "numVertices": self.numVertices,
            "numTriangles": self.numTriangles,
            "bufferLayout": self.bufferLayout,
        })
