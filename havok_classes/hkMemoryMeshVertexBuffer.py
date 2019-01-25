from .hkMeshVertexBuffer import hkMeshVertexBuffer
from .hkVertexFormat import hkVertexFormat
import struct
from .common import any


class hkMemoryMeshVertexBuffer(hkMeshVertexBuffer):
    format: hkVertexFormat
    elementOffsets: int
    memory: any
    vertexStride: int
    locked: bool
    numVertices: int
    isBigEndian: bool
    isSharable: bool

    def __init__(self, infile):
        self.format = hkVertexFormat(infile)  # TYPE_STRUCT
        self.elementOffsets = struct.unpack('>i', infile.read(4))
        self.memory = any(infile)  # TYPE_ARRAY
        self.vertexStride = struct.unpack('>i', infile.read(4))
        self.locked = struct.unpack('>?', infile.read(1))
        self.numVertices = struct.unpack('>i', infile.read(4))
        self.isBigEndian = struct.unpack('>?', infile.read(1))
        self.isSharable = struct.unpack('>?', infile.read(1))
