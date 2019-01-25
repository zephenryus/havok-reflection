from typing import List
from .common import get_array
import struct


class hkxVertexBufferVertexData(object):
    vectorData: List[int]
    floatData: List[int]
    uint32Data: List[int]
    uint16Data: List[int]
    uint8Data: List[int]
    numVerts: int
    vectorStride: int
    floatStride: int
    uint32Stride: int
    uint16Stride: int
    uint8Stride: int

    def __init__(self, infile):
        self.vectorData = get_array(infile, int, 4)  # TYPE_ARRAY:TYPE_UINT32
        self.floatData = get_array(infile, int, 4)  # TYPE_ARRAY:TYPE_UINT32
        self.uint32Data = get_array(infile, int, 4)  # TYPE_ARRAY:TYPE_UINT32
        self.uint16Data = get_array(infile, int, 2)  # TYPE_ARRAY:TYPE_UINT16
        self.uint8Data = get_array(infile, int, 1)  # TYPE_ARRAY:TYPE_UINT8
        self.numVerts = struct.unpack('>I', infile.read(4))  # TYPE_UINT32:TYPE_VOID
        self.vectorStride = struct.unpack('>I', infile.read(4))  # TYPE_UINT32:TYPE_VOID
        self.floatStride = struct.unpack('>I', infile.read(4))  # TYPE_UINT32:TYPE_VOID
        self.uint32Stride = struct.unpack('>I', infile.read(4))  # TYPE_UINT32:TYPE_VOID
        self.uint16Stride = struct.unpack('>I', infile.read(4))  # TYPE_UINT32:TYPE_VOID
        self.uint8Stride = struct.unpack('>I', infile.read(4))  # TYPE_UINT32:TYPE_VOID

    def __repr__(self):
        return "<{class_name} vectorData=[{vectorData}], floatData=[{floatData}], uint32Data=[{uint32Data}], uint16Data=[{uint16Data}], uint8Data=[{uint8Data}], numVerts={numVerts}, vectorStride={vectorStride}, floatStride={floatStride}, uint32Stride={uint32Stride}, uint16Stride={uint16Stride}, uint8Stride={uint8Stride}>".format(**{
            "class_name": self.__class__.__name__,
            "vectorData": self.vectorData,
            "floatData": self.floatData,
            "uint32Data": self.uint32Data,
            "uint16Data": self.uint16Data,
            "uint8Data": self.uint8Data,
            "numVerts": self.numVerts,
            "vectorStride": self.vectorStride,
            "floatStride": self.floatStride,
            "uint32Stride": self.uint32Stride,
            "uint16Stride": self.uint16Stride,
            "uint8Stride": self.uint8Stride,
        })
