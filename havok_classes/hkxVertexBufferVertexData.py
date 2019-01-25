from .common import any
import struct


class hkxVertexBufferVertexData(object):
    vectorData: any
    floatData: any
    uint32Data: any
    uint16Data: any
    uint8Data: any
    numVerts: int
    vectorStride: int
    floatStride: int
    uint32Stride: int
    uint16Stride: int
    uint8Stride: int

    def __init__(self, infile):
        self.vectorData = any(infile)  # TYPE_ARRAY
        self.floatData = any(infile)  # TYPE_ARRAY
        self.uint32Data = any(infile)  # TYPE_ARRAY
        self.uint16Data = any(infile)  # TYPE_ARRAY
        self.uint8Data = any(infile)  # TYPE_ARRAY
        self.numVerts = struct.unpack('>I', infile.read(4))
        self.vectorStride = struct.unpack('>I', infile.read(4))
        self.floatStride = struct.unpack('>I', infile.read(4))
        self.uint32Stride = struct.unpack('>I', infile.read(4))
        self.uint16Stride = struct.unpack('>I', infile.read(4))
        self.uint8Stride = struct.unpack('>I', infile.read(4))
