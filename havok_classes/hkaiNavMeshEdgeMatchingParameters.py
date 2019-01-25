import struct


class hkaiNavMeshEdgeMatchingParameters(object):
    maxStepHeight: float
    maxSeparation: float
    maxOverhang: float
    behindFaceTolerance: float
    cosPlanarAlignmentAngle: float
    cosVerticalAlignmentAngle: float
    minEdgeOverlap: float
    edgeTraversibilityHorizontalEpsilon: float
    edgeTraversibilityVerticalEpsilon: float
    cosClimbingFaceNormalAlignmentAngle: float
    cosClimbingEdgeAlignmentAngle: float
    minAngleBetweenFaces: float
    edgeParallelTolerance: float
    useSafeEdgeTraversibilityHorizontalEpsilon: bool

    def __init__(self, infile):
        self.maxStepHeight = struct.unpack('>f', infile.read(4))
        self.maxSeparation = struct.unpack('>f', infile.read(4))
        self.maxOverhang = struct.unpack('>f', infile.read(4))
        self.behindFaceTolerance = struct.unpack('>f', infile.read(4))
        self.cosPlanarAlignmentAngle = struct.unpack('>f', infile.read(4))
        self.cosVerticalAlignmentAngle = struct.unpack('>f', infile.read(4))
        self.minEdgeOverlap = struct.unpack('>f', infile.read(4))
        self.edgeTraversibilityHorizontalEpsilon = struct.unpack('>f', infile.read(4))
        self.edgeTraversibilityVerticalEpsilon = struct.unpack('>f', infile.read(4))
        self.cosClimbingFaceNormalAlignmentAngle = struct.unpack('>f', infile.read(4))
        self.cosClimbingEdgeAlignmentAngle = struct.unpack('>f', infile.read(4))
        self.minAngleBetweenFaces = struct.unpack('>f', infile.read(4))
        self.edgeParallelTolerance = struct.unpack('>f', infile.read(4))
        self.useSafeEdgeTraversibilityHorizontalEpsilon = struct.unpack('>?', infile.read(1))
