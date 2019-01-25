import struct
from .hclBufferUsage import hclBufferUsage


class hclClothStateBufferAccess(object):
    bufferIndex: int
    bufferUsage: hclBufferUsage
    shadowBufferIndex: int

    def __init__(self, infile):
        self.bufferIndex = struct.unpack('>I', infile.read(4))
        self.bufferUsage = hclBufferUsage(infile)  # TYPE_STRUCT
        self.shadowBufferIndex = struct.unpack('>I', infile.read(4))
