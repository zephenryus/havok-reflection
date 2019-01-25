from enum import Enum
import struct
from .hkaiAgentTraversalInfo import hkaiAgentTraversalInfo
from .hkaiAstarCostModifier import hkaiAstarCostModifier
from .hkaiAstarEdgeFilter import hkaiAstarEdgeFilter
from .enums import QueryMode


class QueryMode(Enum):
    MODE_LINE_OF_SIGHT = 0
    MODE_DIRECT_PATH = 1


class hkaiLineOfSightUtilInputBase(object):
    startPoint: vector4
    up: vector4
    startFaceKey: int
    maxNumberOfIterations: int
    agentInfo: hkaiAgentTraversalInfo
    searchRadius: float
    maximumPathLength: float
    costModifier: any
    edgeFilter: any
    outputEdgesOnFailure: bool
    projectedRadiusCheck: bool
    exactInternalVertexHandling: bool
    isWallClimbing: bool
    mode: QueryMode
    userEdgeHandling: any
    ignoreBackfacingEdges: bool

    def __init__(self, infile):
        self.startPoint = struct.unpack('>4f', infile.read(16))  # TYPE_VECTOR4:TYPE_VOID
        self.up = struct.unpack('>4f', infile.read(16))  # TYPE_VECTOR4:TYPE_VOID
        self.startFaceKey = struct.unpack('>I', infile.read(4))  # TYPE_UINT32:TYPE_VOID
        self.maxNumberOfIterations = struct.unpack('>i', infile.read(4))  # TYPE_INT32:TYPE_VOID
        self.agentInfo = hkaiAgentTraversalInfo(infile)  # TYPE_STRUCT:TYPE_VOID
        self.searchRadius = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.maximumPathLength = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.costModifier = any(infile)  # TYPE_POINTER:TYPE_STRUCT
        self.edgeFilter = any(infile)  # TYPE_POINTER:TYPE_STRUCT
        self.outputEdgesOnFailure = struct.unpack('>?', infile.read(1))  # TYPE_BOOL:TYPE_VOID
        self.projectedRadiusCheck = struct.unpack('>?', infile.read(1))  # TYPE_BOOL:TYPE_VOID
        self.exactInternalVertexHandling = struct.unpack('>?', infile.read(1))  # TYPE_BOOL:TYPE_VOID
        self.isWallClimbing = struct.unpack('>?', infile.read(1))  # TYPE_BOOL:TYPE_VOID
        self.mode = QueryMode(infile)  # TYPE_ENUM:TYPE_UINT8
        self.userEdgeHandling = any(infile)  # TYPE_FLAGS:TYPE_UINT8
        self.ignoreBackfacingEdges = struct.unpack('>?', infile.read(1))  # TYPE_BOOL:TYPE_VOID

    def __repr__(self):
        return "<{class_name} startPoint={startPoint}, up={up}, startFaceKey={startFaceKey}, maxNumberOfIterations={maxNumberOfIterations}, agentInfo={agentInfo}, searchRadius={searchRadius}, maximumPathLength={maximumPathLength}, costModifier={costModifier}, edgeFilter={edgeFilter}, outputEdgesOnFailure={outputEdgesOnFailure}, projectedRadiusCheck={projectedRadiusCheck}, exactInternalVertexHandling={exactInternalVertexHandling}, isWallClimbing={isWallClimbing}, mode={mode}, userEdgeHandling={userEdgeHandling}, ignoreBackfacingEdges={ignoreBackfacingEdges}>".format(**{
            "class_name": self.__class__.__name__,
            "startPoint": self.startPoint,
            "up": self.up,
            "startFaceKey": self.startFaceKey,
            "maxNumberOfIterations": self.maxNumberOfIterations,
            "agentInfo": self.agentInfo,
            "searchRadius": self.searchRadius,
            "maximumPathLength": self.maximumPathLength,
            "costModifier": self.costModifier,
            "edgeFilter": self.edgeFilter,
            "outputEdgesOnFailure": self.outputEdgesOnFailure,
            "projectedRadiusCheck": self.projectedRadiusCheck,
            "exactInternalVertexHandling": self.exactInternalVertexHandling,
            "isWallClimbing": self.isWallClimbing,
            "mode": self.mode,
            "userEdgeHandling": self.userEdgeHandling,
            "ignoreBackfacingEdges": self.ignoreBackfacingEdges,
        })
