from .hkMeshVertexBuffer import hkMeshVertexBuffer
import struct


class hkMultipleVertexBufferVertexBufferInfo(object):
    vertexBuffer: any
    lockedVertices: any
    isLocked: bool

    def __init__(self, infile):
        self.vertexBuffer = any(infile)  # TYPE_POINTER:TYPE_STRUCT
        self.lockedVertices = any(infile)  # TYPE_POINTER:TYPE_VOID
        self.isLocked = struct.unpack('>?', infile.read(1))  # TYPE_BOOL:TYPE_VOID

    def __repr__(self):
        return "<{class_name} vertexBuffer={vertexBuffer}, lockedVertices={lockedVertices}, isLocked={isLocked}>".format(**{
            "class_name": self.__class__.__name__,
            "vertexBuffer": self.vertexBuffer,
            "lockedVertices": self.lockedVertices,
            "isLocked": self.isLocked,
        })
