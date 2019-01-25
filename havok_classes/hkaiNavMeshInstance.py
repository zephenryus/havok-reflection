from .hkReferencedObject import hkReferencedObject
from enum import Enum
from .common import any
import struct
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

    def __init__(self, infile):
        self.originalFaces = any(infile)  # TYPE_SIMPLEARRAY
        self.originalEdges = any(infile)  # TYPE_SIMPLEARRAY
        self.originalVertices = any(infile)  # TYPE_SIMPLEARRAY
        self.originalFaceData = any(infile)  # TYPE_POINTER
        self.faceDataStriding = struct.unpack('>i', infile.read(4))
        self.originalEdgeData = any(infile)  # TYPE_POINTER
        self.edgeDataStriding = struct.unpack('>i', infile.read(4))
        self.originalMesh = hkaiNavMesh(infile)  # TYPE_POINTER
        self.referenceFrame = hkaiReferenceFrame(infile)  # TYPE_STRUCT
        self.edgeMap = any(infile)  # TYPE_ARRAY
        self.faceMap = any(infile)  # TYPE_ARRAY
        self.instancedFaces = hkaiNavMeshFace(infile)  # TYPE_ARRAY
        self.instancedEdges = hkaiNavMeshEdge(infile)  # TYPE_ARRAY
        self.ownedFaces = hkaiNavMeshFace(infile)  # TYPE_ARRAY
        self.ownedEdges = hkaiNavMeshEdge(infile)  # TYPE_ARRAY
        self.ownedVertices = any(infile)  # TYPE_ARRAY
        self.faceFlags = any(infile)  # TYPE_ARRAY
        self.cuttingInfo = any(infile)  # TYPE_ARRAY
        self.instancedFaceData = any(infile)  # TYPE_ARRAY
        self.instancedEdgeData = any(infile)  # TYPE_ARRAY
        self.ownedFaceData = any(infile)  # TYPE_ARRAY
        self.ownedEdgeData = any(infile)  # TYPE_ARRAY
        self.sectionUid = struct.unpack('>I', infile.read(4))
        self.runtimeId = struct.unpack('>i', infile.read(4))
        self.layer = struct.unpack('>I', infile.read(4))
        self.clearanceCaches = hkaiNavMeshClearanceCache(infile)  # TYPE_ARRAY
