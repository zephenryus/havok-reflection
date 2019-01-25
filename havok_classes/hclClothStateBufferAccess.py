import struct
from .hclBufferUsage import hclBufferUsage


class hclClothStateBufferAccess(object):
    bufferIndex: int
    bufferUsage: hclBufferUsage
    shadowBufferIndex: int

    def __init__(self, infile):
        self.bufferIndex = struct.unpack('>I', infile.read(4))  # TYPE_UINT32:TYPE_VOID
        self.bufferUsage = hclBufferUsage(infile)  # TYPE_STRUCT:TYPE_VOID
        self.shadowBufferIndex = struct.unpack('>I', infile.read(4))  # TYPE_UINT32:TYPE_VOID

    def __repr__(self):
        return "<{class_name} bufferIndex={bufferIndex}, bufferUsage={bufferUsage}, shadowBufferIndex={shadowBufferIndex}>".format(**{
            "class_name": self.__class__.__name__,
            "bufferIndex": self.bufferIndex,
            "bufferUsage": self.bufferUsage,
            "shadowBufferIndex": self.shadowBufferIndex,
        })
