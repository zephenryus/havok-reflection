from .hkReferencedObject import hkReferencedObject
from enum import Enum
from typing import List
from .common import get_array
from .hkaiNavMeshCutterMeshInfo import hkaiNavMeshCutterMeshInfo
from .hkaiNavMeshCutterSavedConnectivity import hkaiNavMeshCutterSavedConnectivity
from .hkaiStreamingCollection import hkaiStreamingCollection
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
    meshInfos: List[hkaiNavMeshCutterMeshInfo]
    connectivityInfo: hkaiNavMeshCutterSavedConnectivity
    streamingCollection: any
    forceRecutFaceKeys: List[int]
    forceClearanceCalcFaceKeys: List[int]
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
        self.meshInfos = get_array(infile, hkaiNavMeshCutterMeshInfo, 0)  # TYPE_ARRAY:TYPE_STRUCT
        self.connectivityInfo = hkaiNavMeshCutterSavedConnectivity(infile)  # TYPE_STRUCT:TYPE_VOID
        self.streamingCollection = any(infile)  # TYPE_POINTER:TYPE_STRUCT
        self.forceRecutFaceKeys = get_array(infile, int, 4)  # TYPE_ARRAY:TYPE_UINT32
        self.forceClearanceCalcFaceKeys = get_array(infile, int, 4)  # TYPE_ARRAY:TYPE_UINT32
        self.up = struct.unpack('>4f', infile.read(16))  # TYPE_VECTOR4:TYPE_VOID
        self.edgeMatchParams = hkaiNavMeshEdgeMatchingParameters(infile)  # TYPE_STRUCT:TYPE_VOID
        self.generationSettings = any(infile)  # TYPE_POINTER:TYPE_VOID
        self.cutEdgeTolerance = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.minEdgeMatchingLength = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.smallGapFixupTolerance = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.performValidationChecks = struct.unpack('>?', infile.read(1))  # TYPE_BOOL:TYPE_VOID
        self.clearanceResetMethod = ClearanceResetMethod(infile)  # TYPE_ENUM:TYPE_UINT8
        self.useNewCutter = struct.unpack('>?', infile.read(1))  # TYPE_BOOL:TYPE_VOID
        self.domainQuantum = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID

    def __repr__(self):
        return "<{class_name} meshInfos=[{meshInfos}], connectivityInfo={connectivityInfo}, streamingCollection={streamingCollection}, forceRecutFaceKeys=[{forceRecutFaceKeys}], forceClearanceCalcFaceKeys=[{forceClearanceCalcFaceKeys}], up={up}, edgeMatchParams={edgeMatchParams}, generationSettings={generationSettings}, cutEdgeTolerance={cutEdgeTolerance}, minEdgeMatchingLength={minEdgeMatchingLength}, smallGapFixupTolerance={smallGapFixupTolerance}, performValidationChecks={performValidationChecks}, clearanceResetMethod={clearanceResetMethod}, useNewCutter={useNewCutter}, domainQuantum={domainQuantum}>".format(**{
            "class_name": self.__class__.__name__,
            "meshInfos": self.meshInfos,
            "connectivityInfo": self.connectivityInfo,
            "streamingCollection": self.streamingCollection,
            "forceRecutFaceKeys": self.forceRecutFaceKeys,
            "forceClearanceCalcFaceKeys": self.forceClearanceCalcFaceKeys,
            "up": self.up,
            "edgeMatchParams": self.edgeMatchParams,
            "generationSettings": self.generationSettings,
            "cutEdgeTolerance": self.cutEdgeTolerance,
            "minEdgeMatchingLength": self.minEdgeMatchingLength,
            "smallGapFixupTolerance": self.smallGapFixupTolerance,
            "performValidationChecks": self.performValidationChecks,
            "clearanceResetMethod": self.clearanceResetMethod,
            "useNewCutter": self.useNewCutter,
            "domainQuantum": self.domainQuantum,
        })
