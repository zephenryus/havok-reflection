from .common import any, vector4
import struct


class hkaiLineOfSightUtilLineOfSightOutput(object):
    visitedEdgesOut: any
    distancesOut: any
    pointsOut: any
    doNotExceedArrayCapacity: bool
    numIterationsOut: int
    finalFaceKey: int
    accumulatedDistance: float
    finalPoint: vector4

    def __init__(self, infile):
        self.visitedEdgesOut = any(infile)  # TYPE_ARRAY
        self.distancesOut = any(infile)  # TYPE_ARRAY
        self.pointsOut = any(infile)  # TYPE_ARRAY
        self.doNotExceedArrayCapacity = struct.unpack('>?', infile.read(1))
        self.numIterationsOut = struct.unpack('>i', infile.read(4))
        self.finalFaceKey = struct.unpack('>I', infile.read(4))
        self.accumulatedDistance = struct.unpack('>f', infile.read(4))
        self.finalPoint = struct.unpack('>4f', infile.read(16))
