from .hkReferencedObject import hkReferencedObject
from enum import Enum
from .hkaiNavMeshCutterMeshInfo import hkaiNavMeshCutterMeshInfo
from .hkaiNavMeshCutterSavedConnectivity import hkaiNavMeshCutterSavedConnectivity
from .hkaiStreamingCollection import hkaiStreamingCollection
from .common import any, vector4
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
