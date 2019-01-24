from .hkMeshVertexBuffer import hkMeshVertexBuffer
from .hkVertexFormat import hkVertexFormat
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
