from enum import Enum
from .common import vector4, any
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
