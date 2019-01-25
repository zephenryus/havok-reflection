from .hclShape import hclShape
from .common import any, vector4
from .hkAabb import hkAabb
import struct


class hclConvexPlanesShape(hclShape):
    planeEquations: any
    localFromWorld: any
    worldFromLocal: any
    objAabb: hkAabb
    geomCentroid: vector4

    def __init__(self, infile):
        self.planeEquations = any(infile)  # TYPE_ARRAY
        self.localFromWorld = any(infile)  # TYPE_TRANSFORM
        self.worldFromLocal = any(infile)  # TYPE_TRANSFORM
        self.objAabb = hkAabb(infile)  # TYPE_STRUCT
        self.geomCentroid = struct.unpack('>4f', infile.read(16))
