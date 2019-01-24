from .common import any, vector4


class hkaiLineOfSightUtilLineOfSightOutput(object):
    visitedEdgesOut: any
    distancesOut: any
    pointsOut: any
    doNotExceedArrayCapacity: bool
    numIterationsOut: int
    finalFaceKey: int
    accumulatedDistance: float
    finalPoint: vector4
