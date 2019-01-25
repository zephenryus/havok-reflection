from .hkMeshVertexBuffer import hkMeshVertexBuffer
from .common import any
import struct


class hkMultipleVertexBufferVertexBufferInfo(object):
    vertexBuffer: hkMeshVertexBuffer
    lockedVertices: any
    isLocked: bool

    def __init__(self, infile):
        self.vertexBuffer = hkMeshVertexBuffer(infile)  # TYPE_POINTER
        self.lockedVertices = any(infile)  # TYPE_POINTER
        self.isLocked = struct.unpack('>?', infile.read(1))
