from typing import List
from .common import get_array
import struct


class hkaiLineOfSightUtilLineOfSightOutput(object):
    visitedEdgesOut: List[int]
    distancesOut: List[float]
    pointsOut: List[vector4]
    doNotExceedArrayCapacity: bool
    numIterationsOut: int
    finalFaceKey: int
    accumulatedDistance: float
    finalPoint: vector4

    def __init__(self, infile):
        self.visitedEdgesOut = get_array(infile, int, 4)  # TYPE_ARRAY:TYPE_UINT32
        self.distancesOut = get_array(infile, float, 4)  # TYPE_ARRAY:TYPE_REAL
        self.pointsOut = get_array(infile, vector4, 16)  # TYPE_ARRAY:TYPE_VECTOR4
        self.doNotExceedArrayCapacity = struct.unpack('>?', infile.read(1))  # TYPE_BOOL:TYPE_VOID
        self.numIterationsOut = struct.unpack('>i', infile.read(4))  # TYPE_INT32:TYPE_VOID
        self.finalFaceKey = struct.unpack('>I', infile.read(4))  # TYPE_UINT32:TYPE_VOID
        self.accumulatedDistance = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.finalPoint = struct.unpack('>4f', infile.read(16))  # TYPE_VECTOR4:TYPE_VOID

    def __repr__(self):
        return "<{class_name} visitedEdgesOut=[{visitedEdgesOut}], distancesOut=[{distancesOut}], pointsOut=[{pointsOut}], doNotExceedArrayCapacity={doNotExceedArrayCapacity}, numIterationsOut={numIterationsOut}, finalFaceKey={finalFaceKey}, accumulatedDistance={accumulatedDistance}, finalPoint={finalPoint}>".format(**{
            "class_name": self.__class__.__name__,
            "visitedEdgesOut": self.visitedEdgesOut,
            "distancesOut": self.distancesOut,
            "pointsOut": self.pointsOut,
            "doNotExceedArrayCapacity": self.doNotExceedArrayCapacity,
            "numIterationsOut": self.numIterationsOut,
            "finalFaceKey": self.finalFaceKey,
            "accumulatedDistance": self.accumulatedDistance,
            "finalPoint": self.finalPoint,
        })
