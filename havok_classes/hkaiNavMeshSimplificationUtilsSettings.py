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
        self.maxBorderSimplifyArea = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.maxConcaveBorderSimplifyArea = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.minCorridorWidth = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.maxCorridorWidth = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.holeReplacementArea = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.aabbReplacementAreaFraction = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.maxLoopShrinkFraction = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.maxBorderHeightError = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.maxBorderDistanceError = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.maxPartitionSize = struct.unpack('>i', infile.read(4))  # TYPE_INT32:TYPE_VOID
        self.useHeightPartitioning = struct.unpack('>?', infile.read(1))  # TYPE_BOOL:TYPE_VOID
        self.maxPartitionHeightError = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.useConservativeHeightPartitioning = struct.unpack('>?', infile.read(1))  # TYPE_BOOL:TYPE_VOID
        self.hertelMehlhornHeightError = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.cosPlanarityThreshold = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.nonconvexityThreshold = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.boundaryEdgeFilterThreshold = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.maxSharedVertexHorizontalError = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.maxSharedVertexVerticalError = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.maxBoundaryVertexHorizontalError = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.maxBoundaryVertexVerticalError = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.mergeLongestEdgesFirst = struct.unpack('>?', infile.read(1))  # TYPE_BOOL:TYPE_VOID
        self.extraVertexSettings = hkaiNavMeshSimplificationUtilsExtraVertexSettings(infile)  # TYPE_STRUCT:TYPE_VOID
        self.saveInputSnapshot = struct.unpack('>?', infile.read(1))  # TYPE_BOOL:TYPE_VOID
        self.snapshotFilename = struct.unpack('>s', infile.read(0))  # TYPE_STRINGPTR:TYPE_VOID

    def __repr__(self):
        return "<{class_name} maxBorderSimplifyArea={maxBorderSimplifyArea}, maxConcaveBorderSimplifyArea={maxConcaveBorderSimplifyArea}, minCorridorWidth={minCorridorWidth}, maxCorridorWidth={maxCorridorWidth}, holeReplacementArea={holeReplacementArea}, aabbReplacementAreaFraction={aabbReplacementAreaFraction}, maxLoopShrinkFraction={maxLoopShrinkFraction}, maxBorderHeightError={maxBorderHeightError}, maxBorderDistanceError={maxBorderDistanceError}, maxPartitionSize={maxPartitionSize}, useHeightPartitioning={useHeightPartitioning}, maxPartitionHeightError={maxPartitionHeightError}, useConservativeHeightPartitioning={useConservativeHeightPartitioning}, hertelMehlhornHeightError={hertelMehlhornHeightError}, cosPlanarityThreshold={cosPlanarityThreshold}, nonconvexityThreshold={nonconvexityThreshold}, boundaryEdgeFilterThreshold={boundaryEdgeFilterThreshold}, maxSharedVertexHorizontalError={maxSharedVertexHorizontalError}, maxSharedVertexVerticalError={maxSharedVertexVerticalError}, maxBoundaryVertexHorizontalError={maxBoundaryVertexHorizontalError}, maxBoundaryVertexVerticalError={maxBoundaryVertexVerticalError}, mergeLongestEdgesFirst={mergeLongestEdgesFirst}, extraVertexSettings={extraVertexSettings}, saveInputSnapshot={saveInputSnapshot}, snapshotFilename=\"{snapshotFilename}\">".format(**{
            "class_name": self.__class__.__name__,
            "maxBorderSimplifyArea": self.maxBorderSimplifyArea,
            "maxConcaveBorderSimplifyArea": self.maxConcaveBorderSimplifyArea,
            "minCorridorWidth": self.minCorridorWidth,
            "maxCorridorWidth": self.maxCorridorWidth,
            "holeReplacementArea": self.holeReplacementArea,
            "aabbReplacementAreaFraction": self.aabbReplacementAreaFraction,
            "maxLoopShrinkFraction": self.maxLoopShrinkFraction,
            "maxBorderHeightError": self.maxBorderHeightError,
            "maxBorderDistanceError": self.maxBorderDistanceError,
            "maxPartitionSize": self.maxPartitionSize,
            "useHeightPartitioning": self.useHeightPartitioning,
            "maxPartitionHeightError": self.maxPartitionHeightError,
            "useConservativeHeightPartitioning": self.useConservativeHeightPartitioning,
            "hertelMehlhornHeightError": self.hertelMehlhornHeightError,
            "cosPlanarityThreshold": self.cosPlanarityThreshold,
            "nonconvexityThreshold": self.nonconvexityThreshold,
            "boundaryEdgeFilterThreshold": self.boundaryEdgeFilterThreshold,
            "maxSharedVertexHorizontalError": self.maxSharedVertexHorizontalError,
            "maxSharedVertexVerticalError": self.maxSharedVertexVerticalError,
            "maxBoundaryVertexHorizontalError": self.maxBoundaryVertexHorizontalError,
            "maxBoundaryVertexVerticalError": self.maxBoundaryVertexVerticalError,
            "mergeLongestEdgesFirst": self.mergeLongestEdgesFirst,
            "extraVertexSettings": self.extraVertexSettings,
            "saveInputSnapshot": self.saveInputSnapshot,
            "snapshotFilename": self.snapshotFilename,
        })
