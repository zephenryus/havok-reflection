from .hkReferencedObject import hkReferencedObject
from enum import Enum
from .common import any
from .hkaiNavMesh import hkaiNavMesh
from .hkaiReferenceFrame import hkaiReferenceFrame
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
    originalMesh: hkaiNavMesh
    referenceFrame: hkaiReferenceFrame
    edgeMap: any
    faceMap: any
    instancedFaces: hkaiNavMeshFace
    instancedEdges: hkaiNavMeshEdge
    ownedFaces: hkaiNavMeshFace
    ownedEdges: hkaiNavMeshEdge
    ownedVertices: any
    faceFlags: any
    cuttingInfo: any
    instancedFaceData: any
    instancedEdgeData: any
    ownedFaceData: any
    ownedEdgeData: any
    sectionUid: int
    runtimeId: int
    layer: int
    clearanceCaches: hkaiNavMeshClearanceCache
