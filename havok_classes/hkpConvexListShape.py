from .hkpConvexShape import hkpConvexShape
import struct
from .common import vector4


class hkpConvexListShape(hkpConvexShape):
    minDistanceToUseConvexHullForGetClosestPoints: float
    aabbHalfExtents: vector4
    aabbCenter: vector4
    useCachedAabb: bool
    childShapes: hkpConvexShape

    def __init__(self, infile):
        self.minDistanceToUseConvexHullForGetClosestPoints = struct.unpack('>f', infile.read(4))
        self.aabbHalfExtents = struct.unpack('>4f', infile.read(16))
        self.aabbCenter = struct.unpack('>4f', infile.read(16))
        self.useCachedAabb = struct.unpack('>?', infile.read(1))
        self.childShapes = hkpConvexShape(infile)  # TYPE_ARRAY
