from enum import Enum
from .common import vector4, any
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
    costModifier: hkaiAstarCostModifier
    edgeFilter: hkaiAstarEdgeFilter
    outputEdgesOnFailure: bool
    projectedRadiusCheck: bool
    exactInternalVertexHandling: bool
    isWallClimbing: bool
    mode: QueryMode
    userEdgeHandling: any
    ignoreBackfacingEdges: bool

    def __init__(self, infile):
        self.startPoint = struct.unpack('>4f', infile.read(16))
        self.up = struct.unpack('>4f', infile.read(16))
        self.startFaceKey = struct.unpack('>I', infile.read(4))
        self.maxNumberOfIterations = struct.unpack('>i', infile.read(4))
        self.agentInfo = hkaiAgentTraversalInfo(infile)  # TYPE_STRUCT
        self.searchRadius = struct.unpack('>f', infile.read(4))
        self.maximumPathLength = struct.unpack('>f', infile.read(4))
        self.costModifier = hkaiAstarCostModifier(infile)  # TYPE_POINTER
        self.edgeFilter = hkaiAstarEdgeFilter(infile)  # TYPE_POINTER
        self.outputEdgesOnFailure = struct.unpack('>?', infile.read(1))
        self.projectedRadiusCheck = struct.unpack('>?', infile.read(1))
        self.exactInternalVertexHandling = struct.unpack('>?', infile.read(1))
        self.isWallClimbing = struct.unpack('>?', infile.read(1))
        self.mode = QueryMode(infile)  # TYPE_ENUM
        self.userEdgeHandling = any(infile)  # TYPE_FLAGS
        self.ignoreBackfacingEdges = struct.unpack('>?', infile.read(1))
