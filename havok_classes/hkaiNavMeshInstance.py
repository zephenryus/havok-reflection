from .hkReferencedObject import hkReferencedObject
from enum import Enum
import struct
from .hkaiNavMesh import hkaiNavMesh
from .hkaiReferenceFrame import hkaiReferenceFrame
from typing import List
from .common import get_array
from .hkaiNavMeshFace import hkaiNavMeshFace
from .hkaiNavMeshEdge import hkaiNavMeshEdge
from .hkaiNavMeshClearanceCache import hkaiNavMeshClearanceCache


class DebugValues(Enum):
    DEAD_FACE = 3735943886
    DEAD_EDGE = 3735940462


class CutInfoValues(Enum):
    NOT_CUT_EDGE = 65535


class hkaiNavMeshInstance(hkReferencedObject):
    originalFaces: any
    originalEdges: any
    originalVertices: any
    originalFaceData: any
    faceDataStriding: int
    originalEdgeData: any
    edgeDataStriding: int
    originalMesh: any
    referenceFrame: hkaiReferenceFrame
    edgeMap: List[int]
    faceMap: List[int]
    instancedFaces: List[hkaiNavMeshFace]
    instancedEdges: List[hkaiNavMeshEdge]
    ownedFaces: List[hkaiNavMeshFace]
    ownedEdges: List[hkaiNavMeshEdge]
    ownedVertices: List[vector4]
    faceFlags: List[int]
    cuttingInfo: List[int]
    instancedFaceData: List[int]
    instancedEdgeData: List[int]
    ownedFaceData: List[int]
    ownedEdgeData: List[int]
    sectionUid: int
    runtimeId: int
    layer: int
    clearanceCaches: List[hkaiNavMeshClearanceCache]

    def __init__(self, infile):
        self.originalFaces = any(infile)  # TYPE_SIMPLEARRAY:TYPE_VOID
        self.originalEdges = any(infile)  # TYPE_SIMPLEARRAY:TYPE_VOID
        self.originalVertices = any(infile)  # TYPE_SIMPLEARRAY:TYPE_VOID
        self.originalFaceData = any(infile)  # TYPE_POINTER:TYPE_VOID
        self.faceDataStriding = struct.unpack('>i', infile.read(4))  # TYPE_INT32:TYPE_VOID
        self.originalEdgeData = any(infile)  # TYPE_POINTER:TYPE_VOID
        self.edgeDataStriding = struct.unpack('>i', infile.read(4))  # TYPE_INT32:TYPE_VOID
        self.originalMesh = any(infile)  # TYPE_POINTER:TYPE_STRUCT
        self.referenceFrame = hkaiReferenceFrame(infile)  # TYPE_STRUCT:TYPE_VOID
        self.edgeMap = get_array(infile, int, 4)  # TYPE_ARRAY:TYPE_INT32
        self.faceMap = get_array(infile, int, 4)  # TYPE_ARRAY:TYPE_INT32
        self.instancedFaces = get_array(infile, hkaiNavMeshFace, 0)  # TYPE_ARRAY:TYPE_STRUCT
        self.instancedEdges = get_array(infile, hkaiNavMeshEdge, 0)  # TYPE_ARRAY:TYPE_STRUCT
        self.ownedFaces = get_array(infile, hkaiNavMeshFace, 0)  # TYPE_ARRAY:TYPE_STRUCT
        self.ownedEdges = get_array(infile, hkaiNavMeshEdge, 0)  # TYPE_ARRAY:TYPE_STRUCT
        self.ownedVertices = get_array(infile, vector4, 16)  # TYPE_ARRAY:TYPE_VECTOR4
        self.faceFlags = get_array(infile, int, 1)  # TYPE_ARRAY:TYPE_UINT8
        self.cuttingInfo = get_array(infile, int, 2)  # TYPE_ARRAY:TYPE_UINT16
        self.instancedFaceData = get_array(infile, int, 4)  # TYPE_ARRAY:TYPE_INT32
        self.instancedEdgeData = get_array(infile, int, 4)  # TYPE_ARRAY:TYPE_INT32
        self.ownedFaceData = get_array(infile, int, 4)  # TYPE_ARRAY:TYPE_INT32
        self.ownedEdgeData = get_array(infile, int, 4)  # TYPE_ARRAY:TYPE_INT32
        self.sectionUid = struct.unpack('>I', infile.read(4))  # TYPE_UINT32:TYPE_VOID
        self.runtimeId = struct.unpack('>i', infile.read(4))  # TYPE_INT32:TYPE_VOID
        self.layer = struct.unpack('>I', infile.read(4))  # TYPE_UINT32:TYPE_VOID
        self.clearanceCaches = get_array(infile, hkaiNavMeshClearanceCache, 0)  # TYPE_ARRAY:TYPE_POINTER

    def __repr__(self):
        return "<{class_name} originalFaces={originalFaces}, originalEdges={originalEdges}, originalVertices={originalVertices}, originalFaceData={originalFaceData}, faceDataStriding={faceDataStriding}, originalEdgeData={originalEdgeData}, edgeDataStriding={edgeDataStriding}, originalMesh={originalMesh}, referenceFrame={referenceFrame}, edgeMap=[{edgeMap}], faceMap=[{faceMap}], instancedFaces=[{instancedFaces}], instancedEdges=[{instancedEdges}], ownedFaces=[{ownedFaces}], ownedEdges=[{ownedEdges}], ownedVertices=[{ownedVertices}], faceFlags=[{faceFlags}], cuttingInfo=[{cuttingInfo}], instancedFaceData=[{instancedFaceData}], instancedEdgeData=[{instancedEdgeData}], ownedFaceData=[{ownedFaceData}], ownedEdgeData=[{ownedEdgeData}], sectionUid={sectionUid}, runtimeId={runtimeId}, layer={layer}, clearanceCaches=[{clearanceCaches}]>".format(**{
            "class_name": self.__class__.__name__,
            "originalFaces": self.originalFaces,
            "originalEdges": self.originalEdges,
            "originalVertices": self.originalVertices,
            "originalFaceData": self.originalFaceData,
            "faceDataStriding": self.faceDataStriding,
            "originalEdgeData": self.originalEdgeData,
            "edgeDataStriding": self.edgeDataStriding,
            "originalMesh": self.originalMesh,
            "referenceFrame": self.referenceFrame,
            "edgeMap": self.edgeMap,
            "faceMap": self.faceMap,
            "instancedFaces": self.instancedFaces,
            "instancedEdges": self.instancedEdges,
            "ownedFaces": self.ownedFaces,
            "ownedEdges": self.ownedEdges,
            "ownedVertices": self.ownedVertices,
            "faceFlags": self.faceFlags,
            "cuttingInfo": self.cuttingInfo,
            "instancedFaceData": self.instancedFaceData,
            "instancedEdgeData": self.instancedEdgeData,
            "ownedFaceData": self.ownedFaceData,
            "ownedEdgeData": self.ownedEdgeData,
            "sectionUid": self.sectionUid,
            "runtimeId": self.runtimeId,
            "layer": self.layer,
            "clearanceCaches": self.clearanceCaches,
        })
