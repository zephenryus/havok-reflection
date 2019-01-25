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
        self.maxStepHeight = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.maxSeparation = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.maxOverhang = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.behindFaceTolerance = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.cosPlanarAlignmentAngle = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.cosVerticalAlignmentAngle = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.minEdgeOverlap = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.edgeTraversibilityHorizontalEpsilon = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.edgeTraversibilityVerticalEpsilon = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.cosClimbingFaceNormalAlignmentAngle = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.cosClimbingEdgeAlignmentAngle = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.minAngleBetweenFaces = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.edgeParallelTolerance = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.useSafeEdgeTraversibilityHorizontalEpsilon = struct.unpack('>?', infile.read(1))  # TYPE_BOOL:TYPE_VOID

    def __repr__(self):
        return "<{class_name} maxStepHeight={maxStepHeight}, maxSeparation={maxSeparation}, maxOverhang={maxOverhang}, behindFaceTolerance={behindFaceTolerance}, cosPlanarAlignmentAngle={cosPlanarAlignmentAngle}, cosVerticalAlignmentAngle={cosVerticalAlignmentAngle}, minEdgeOverlap={minEdgeOverlap}, edgeTraversibilityHorizontalEpsilon={edgeTraversibilityHorizontalEpsilon}, edgeTraversibilityVerticalEpsilon={edgeTraversibilityVerticalEpsilon}, cosClimbingFaceNormalAlignmentAngle={cosClimbingFaceNormalAlignmentAngle}, cosClimbingEdgeAlignmentAngle={cosClimbingEdgeAlignmentAngle}, minAngleBetweenFaces={minAngleBetweenFaces}, edgeParallelTolerance={edgeParallelTolerance}, useSafeEdgeTraversibilityHorizontalEpsilon={useSafeEdgeTraversibilityHorizontalEpsilon}>".format(**{
            "class_name": self.__class__.__name__,
            "maxStepHeight": self.maxStepHeight,
            "maxSeparation": self.maxSeparation,
            "maxOverhang": self.maxOverhang,
            "behindFaceTolerance": self.behindFaceTolerance,
            "cosPlanarAlignmentAngle": self.cosPlanarAlignmentAngle,
            "cosVerticalAlignmentAngle": self.cosVerticalAlignmentAngle,
            "minEdgeOverlap": self.minEdgeOverlap,
            "edgeTraversibilityHorizontalEpsilon": self.edgeTraversibilityHorizontalEpsilon,
            "edgeTraversibilityVerticalEpsilon": self.edgeTraversibilityVerticalEpsilon,
            "cosClimbingFaceNormalAlignmentAngle": self.cosClimbingFaceNormalAlignmentAngle,
            "cosClimbingEdgeAlignmentAngle": self.cosClimbingEdgeAlignmentAngle,
            "minAngleBetweenFaces": self.minAngleBetweenFaces,
            "edgeParallelTolerance": self.edgeParallelTolerance,
            "useSafeEdgeTraversibilityHorizontalEpsilon": self.useSafeEdgeTraversibilityHorizontalEpsilon,
        })
