from .hkMeshVertexBuffer import hkMeshVertexBuffer
from .common import any


class hkMultipleVertexBufferVertexBufferInfo(object):
    vertexBuffer: hkMeshVertexBuffer
    lockedVertices: any
    isLocked: bool
