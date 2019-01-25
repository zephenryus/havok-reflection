from .hkpConvexShape import hkpConvexShape
import struct
from typing import List
from .common import get_array
from .hkpConvexVerticesConnectivity import hkpConvexVerticesConnectivity


class hkpConvexVerticesShape(hkpConvexShape):
    aabbHalfExtents: vector4
    aabbCenter: vector4
    rotatedVertices: List[any]
    numVertices: int
    useSpuBuffer: bool
    planeEquations: List[vector4]
    connectivity: any

    def __init__(self, infile):
        self.aabbHalfExtents = struct.unpack('>4f', infile.read(16))  # TYPE_VECTOR4:TYPE_VOID
        self.aabbCenter = struct.unpack('>4f', infile.read(16))  # TYPE_VECTOR4:TYPE_VOID
        self.rotatedVertices = get_array(infile, any, 0)  # TYPE_ARRAY:TYPE_MATRIX3
        self.numVertices = struct.unpack('>i', infile.read(4))  # TYPE_INT32:TYPE_VOID
        self.useSpuBuffer = struct.unpack('>?', infile.read(1))  # TYPE_BOOL:TYPE_VOID
        self.planeEquations = get_array(infile, vector4, 16)  # TYPE_ARRAY:TYPE_VECTOR4
        self.connectivity = any(infile)  # TYPE_POINTER:TYPE_STRUCT

    def __repr__(self):
        return "<{class_name} aabbHalfExtents={aabbHalfExtents}, aabbCenter={aabbCenter}, rotatedVertices=[{rotatedVertices}], numVertices={numVertices}, useSpuBuffer={useSpuBuffer}, planeEquations=[{planeEquations}], connectivity={connectivity}>".format(**{
            "class_name": self.__class__.__name__,
            "aabbHalfExtents": self.aabbHalfExtents,
            "aabbCenter": self.aabbCenter,
            "rotatedVertices": self.rotatedVertices,
            "numVertices": self.numVertices,
            "useSpuBuffer": self.useSpuBuffer,
            "planeEquations": self.planeEquations,
            "connectivity": self.connectivity,
        })
