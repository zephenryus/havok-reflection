from .hkReferencedObject import hkReferencedObject
from enum import Enum
from .hkaiNavMeshCutterMeshInfo import hkaiNavMeshCutterMeshInfo
from .hkaiNavMeshCutterSavedConnectivity import hkaiNavMeshCutterSavedConnectivity
from .hkaiStreamingCollection import hkaiStreamingCollection
from .common import any, vector4
import struct
from .hkaiNavMeshEdgeMatchingParameters import hkaiNavMeshEdgeMatchingParameters
from .enums import ClearanceResetMethod


class ClearanceResetMethod(Enum):
    CLEARANCE_RESET_ALL = 0
    CLEARANCE_RESET_MEDIATOR = 1
    CLEARANCE_RESET_FLOODFILL = 2


class GatherCutEdgesMode(Enum):
    GATHER_ALL_EDGES = 0
    GATHER_BOUNDARY_EDGES = 1


class hkaiNavMeshCutter(hkReferencedObject):
    meshInfos: hkaiNavMeshCutterMeshInfo
    connectivityInfo: hkaiNavMeshCutterSavedConnectivity
    streamingCollection: hkaiStreamingCollection
    forceRecutFaceKeys: any
    forceClearanceCalcFaceKeys: any
    up: vector4
    edgeMatchParams: hkaiNavMeshEdgeMatchingParameters
    generationSettings: any
    cutEdgeTolerance: float
    minEdgeMatchingLength: float
    smallGapFixupTolerance: float
    performValidationChecks: bool
    clearanceResetMethod: ClearanceResetMethod
    useNewCutter: bool
    domainQuantum: float

    def __init__(self, infile):
        self.meshInfos = hkaiNavMeshCutterMeshInfo(infile)  # TYPE_ARRAY
        self.connectivityInfo = hkaiNavMeshCutterSavedConnectivity(infile)  # TYPE_STRUCT
        self.streamingCollection = hkaiStreamingCollection(infile)  # TYPE_POINTER
        self.forceRecutFaceKeys = any(infile)  # TYPE_ARRAY
        self.forceClearanceCalcFaceKeys = any(infile)  # TYPE_ARRAY
        self.up = struct.unpack('>4f', infile.read(16))
        self.edgeMatchParams = hkaiNavMeshEdgeMatchingParameters(infile)  # TYPE_STRUCT
        self.generationSettings = any(infile)  # TYPE_POINTER
        self.cutEdgeTolerance = struct.unpack('>f', infile.read(4))
        self.minEdgeMatchingLength = struct.unpack('>f', infile.read(4))
        self.smallGapFixupTolerance = struct.unpack('>f', infile.read(4))
        self.performValidationChecks = struct.unpack('>?', infile.read(1))
        self.clearanceResetMethod = ClearanceResetMethod(infile)  # TYPE_ENUM
        self.useNewCutter = struct.unpack('>?', infile.read(1))
        self.domainQuantum = struct.unpack('>f', infile.read(4))
