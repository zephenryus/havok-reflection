import struct
from .hkaiNavMeshSimplificationUtilsExtraVertexSettings import hkaiNavMeshSimplificationUtilsExtraVertexSettings


class hkaiNavMeshSimplificationUtilsSettings(object):
    maxBorderSimplifyArea: float
    maxConcaveBorderSimplifyArea: float
    minCorridorWidth: float
    maxCorridorWidth: float
    holeReplacementArea: float
    aabbReplacementAreaFraction: float
    maxLoopShrinkFraction: float
    maxBorderHeightError: float
    maxBorderDistanceError: float
    maxPartitionSize: int
    useHeightPartitioning: bool
    maxPartitionHeightError: float
    useConservativeHeightPartitioning: bool
    hertelMehlhornHeightError: float
    cosPlanarityThreshold: float
    nonconvexityThreshold: float
    boundaryEdgeFilterThreshold: float
    maxSharedVertexHorizontalError: float
    maxSharedVertexVerticalError: float
    maxBoundaryVertexHorizontalError: float
    maxBoundaryVertexVerticalError: float
    mergeLongestEdgesFirst: bool
    extraVertexSettings: hkaiNavMeshSimplificationUtilsExtraVertexSettings
    saveInputSnapshot: bool
    snapshotFilename: str

    def __init__(self, infile):
        self.maxBorderSimplifyArea = struct.unpack('>f', infile.read(4))
        self.maxConcaveBorderSimplifyArea = struct.unpack('>f', infile.read(4))
        self.minCorridorWidth = struct.unpack('>f', infile.read(4))
        self.maxCorridorWidth = struct.unpack('>f', infile.read(4))
        self.holeReplacementArea = struct.unpack('>f', infile.read(4))
        self.aabbReplacementAreaFraction = struct.unpack('>f', infile.read(4))
        self.maxLoopShrinkFraction = struct.unpack('>f', infile.read(4))
        self.maxBorderHeightError = struct.unpack('>f', infile.read(4))
        self.maxBorderDistanceError = struct.unpack('>f', infile.read(4))
        self.maxPartitionSize = struct.unpack('>i', infile.read(4))
        self.useHeightPartitioning = struct.unpack('>?', infile.read(1))
        self.maxPartitionHeightError = struct.unpack('>f', infile.read(4))
        self.useConservativeHeightPartitioning = struct.unpack('>?', infile.read(1))
        self.hertelMehlhornHeightError = struct.unpack('>f', infile.read(4))
        self.cosPlanarityThreshold = struct.unpack('>f', infile.read(4))
        self.nonconvexityThreshold = struct.unpack('>f', infile.read(4))
        self.boundaryEdgeFilterThreshold = struct.unpack('>f', infile.read(4))
        self.maxSharedVertexHorizontalError = struct.unpack('>f', infile.read(4))
        self.maxSharedVertexVerticalError = struct.unpack('>f', infile.read(4))
        self.maxBoundaryVertexHorizontalError = struct.unpack('>f', infile.read(4))
        self.maxBoundaryVertexVerticalError = struct.unpack('>f', infile.read(4))
        self.mergeLongestEdgesFirst = struct.unpack('>?', infile.read(1))
        self.extraVertexSettings = hkaiNavMeshSimplificationUtilsExtraVertexSettings(infile)  # TYPE_STRUCT
        self.saveInputSnapshot = struct.unpack('>?', infile.read(1))
        self.snapshotFilename = struct.unpack('>s', infile.read(0))
