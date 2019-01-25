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
        self.name = struct.unpack('>s', infile.read(0))
        self.type = struct.unpack('>i', infile.read(4))
        self.subType = struct.unpack('>i', infile.read(4))
        self.numVertices = struct.unpack('>I', infile.read(4))
        self.numTriangles = struct.unpack('>I', infile.read(4))
        self.bufferLayout = hclBufferLayout(infile)  # TYPE_STRUCT
