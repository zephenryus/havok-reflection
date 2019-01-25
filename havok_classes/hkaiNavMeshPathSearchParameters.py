from enum import Enum
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
        self.up = struct.unpack('>4f', infile.read(16))  # TYPE_VECTOR4:TYPE_VOID
        self.costModifier = any(infile)  # TYPE_POINTER:TYPE_VOID
        self.edgeFilter = any(infile)  # TYPE_POINTER:TYPE_VOID
        self.validateInputs = struct.unpack('>?', infile.read(1))  # TYPE_BOOL:TYPE_VOID
        self.outputPathFlags = any(infile)  # TYPE_FLAGS:TYPE_UINT8
        self.lineOfSightFlags = any(infile)  # TYPE_FLAGS:TYPE_UINT8
        self.useHierarchicalHeuristic = struct.unpack('>?', infile.read(1))  # TYPE_BOOL:TYPE_VOID
        self.projectedRadiusCheck = struct.unpack('>?', infile.read(1))  # TYPE_BOOL:TYPE_VOID
        self.useGrandparentDistanceCalculation = struct.unpack('>?', infile.read(1))  # TYPE_BOOL:TYPE_VOID
        self.heuristicWeight = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.simpleRadiusThreshold = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.maximumPathLength = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.searchSphereRadius = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.searchCapsuleRadius = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.bufferSizes = hkaiSearchParametersBufferSizes(infile)  # TYPE_STRUCT:TYPE_VOID
        self.hierarchyBufferSizes = hkaiSearchParametersBufferSizes(infile)  # TYPE_STRUCT:TYPE_VOID

    def __repr__(self):
        return "<{class_name} up={up}, costModifier={costModifier}, edgeFilter={edgeFilter}, validateInputs={validateInputs}, outputPathFlags={outputPathFlags}, lineOfSightFlags={lineOfSightFlags}, useHierarchicalHeuristic={useHierarchicalHeuristic}, projectedRadiusCheck={projectedRadiusCheck}, useGrandparentDistanceCalculation={useGrandparentDistanceCalculation}, heuristicWeight={heuristicWeight}, simpleRadiusThreshold={simpleRadiusThreshold}, maximumPathLength={maximumPathLength}, searchSphereRadius={searchSphereRadius}, searchCapsuleRadius={searchCapsuleRadius}, bufferSizes={bufferSizes}, hierarchyBufferSizes={hierarchyBufferSizes}>".format(**{
            "class_name": self.__class__.__name__,
            "up": self.up,
            "costModifier": self.costModifier,
            "edgeFilter": self.edgeFilter,
            "validateInputs": self.validateInputs,
            "outputPathFlags": self.outputPathFlags,
            "lineOfSightFlags": self.lineOfSightFlags,
            "useHierarchicalHeuristic": self.useHierarchicalHeuristic,
            "projectedRadiusCheck": self.projectedRadiusCheck,
            "useGrandparentDistanceCalculation": self.useGrandparentDistanceCalculation,
            "heuristicWeight": self.heuristicWeight,
            "simpleRadiusThreshold": self.simpleRadiusThreshold,
            "maximumPathLength": self.maximumPathLength,
            "searchSphereRadius": self.searchSphereRadius,
            "searchCapsuleRadius": self.searchCapsuleRadius,
            "bufferSizes": self.bufferSizes,
            "hierarchyBufferSizes": self.hierarchyBufferSizes,
        })
