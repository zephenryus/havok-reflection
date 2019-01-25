from enum import Enum
from .common import vector4, any
import struct
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

    def __init__(self, infile):
        self.up = struct.unpack('>4f', infile.read(16))
        self.costModifier = any(infile)  # TYPE_POINTER
        self.edgeFilter = any(infile)  # TYPE_POINTER
        self.validateInputs = struct.unpack('>?', infile.read(1))
        self.outputPathFlags = any(infile)  # TYPE_FLAGS
        self.lineOfSightFlags = any(infile)  # TYPE_FLAGS
        self.useHierarchicalHeuristic = struct.unpack('>?', infile.read(1))
        self.projectedRadiusCheck = struct.unpack('>?', infile.read(1))
        self.useGrandparentDistanceCalculation = struct.unpack('>?', infile.read(1))
        self.heuristicWeight = struct.unpack('>f', infile.read(4))
        self.simpleRadiusThreshold = struct.unpack('>f', infile.read(4))
        self.maximumPathLength = struct.unpack('>f', infile.read(4))
        self.searchSphereRadius = struct.unpack('>f', infile.read(4))
        self.searchCapsuleRadius = struct.unpack('>f', infile.read(4))
        self.bufferSizes = hkaiSearchParametersBufferSizes(infile)  # TYPE_STRUCT
        self.hierarchyBufferSizes = hkaiSearchParametersBufferSizes(infile)  # TYPE_STRUCT
