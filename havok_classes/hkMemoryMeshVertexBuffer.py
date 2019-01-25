from .hkMeshVertexBuffer import hkMeshVertexBuffer
from .hkVertexFormat import hkVertexFormat
import struct
from typing import List
from .common import get_array


class hkMemoryMeshVertexBuffer(hkMeshVertexBuffer):
    format: hkVertexFormat
    elementOffsets: int
    memory: List[int]
    vertexStride: int
    locked: bool
    numVertices: int
    isBigEndian: bool
    isSharable: bool

    def __init__(self, infile):
        self.format = hkVertexFormat(infile)  # TYPE_STRUCT:TYPE_VOID
        self.elementOffsets = struct.unpack('>i', infile.read(4))  # TYPE_INT32:TYPE_VOID
        self.memory = get_array(infile, int, 1)  # TYPE_ARRAY:TYPE_UINT8
        self.vertexStride = struct.unpack('>i', infile.read(4))  # TYPE_INT32:TYPE_VOID
        self.locked = struct.unpack('>?', infile.read(1))  # TYPE_BOOL:TYPE_VOID
        self.numVertices = struct.unpack('>i', infile.read(4))  # TYPE_INT32:TYPE_VOID
        self.isBigEndian = struct.unpack('>?', infile.read(1))  # TYPE_BOOL:TYPE_VOID
        self.isSharable = struct.unpack('>?', infile.read(1))  # TYPE_BOOL:TYPE_VOID

    def __repr__(self):
        return "<{class_name} format={format}, elementOffsets={elementOffsets}, memory=[{memory}], vertexStride={vertexStride}, locked={locked}, numVertices={numVertices}, isBigEndian={isBigEndian}, isSharable={isSharable}>".format(**{
            "class_name": self.__class__.__name__,
            "format": self.format,
            "elementOffsets": self.elementOffsets,
            "memory": self.memory,
            "vertexStride": self.vertexStride,
            "locked": self.locked,
            "numVertices": self.numVertices,
            "isBigEndian": self.isBigEndian,
            "isSharable": self.isSharable,
        })
