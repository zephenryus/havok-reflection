from enum import Enum
from .common import vector4, any
from .hkaiSearchParametersBufferSizes import hkaiSearchParametersBufferSizes


class OutputPathFlags(Enum):
    OUTPUT_PATH_SMOOTHED = 1
    OUTPUT_PATH_PROJECTED = 2
    OUTPUT_PATH_COMPUTE_NORMALS = 4


class LineOfSightFlags(Enum):
    NO_LINE_OF_SIGHT_CHECK = 0
    EARLY_OUT_IF_NO_COST_MODIFIER = 1
    HANDLE_INTERNAL_VERTICES = 2
    EARLY_OUT_ALWAYS = 4


class hkaiNavMeshPathSearchParameters(object):
    up: vector4
    costModifier: any
    edgeFilter: any
    validateInputs: bool
    outputPathFlags: any
    lineOfSightFlags: any
    useHierarchicalHeuristic: bool
    projectedRadiusCheck: bool
    useGrandparentDistanceCalculation: bool
    heuristicWeight: float
    simpleRadiusThreshold: float
    maximumPathLength: float
    searchSphereRadius: float
    searchCapsuleRadius: float
    bufferSizes: hkaiSearchParametersBufferSizes
    hierarchyBufferSizes: hkaiSearchParametersBufferSizes
