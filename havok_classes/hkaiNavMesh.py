from .hkReferencedObject import hkReferencedObject
from enum import Enum
from .hkaiNavMeshFace import hkaiNavMeshFace
from .hkaiNavMeshEdge import hkaiNavMeshEdge
from .common import any
from .hkaiStreamingSet import hkaiStreamingSet
from .hkAabb import hkAabb


class FaceFlagBits(Enum):
    FACE_HIDDEN = 1
    FACE_CUT = 2
    FACE_STREAMING = 4


class NavMeshFlagBits(Enum):
    MESH_NONE = 0
    MESH_CLIMBING = 1


class Constants(Enum):
    INVALID_REGION_INDEX = 4294967295
    INVALID_FACE_INDEX = 4294967295
    INVALID_EDGE_INDEX = 4294967295
    INVALID_VERTEX_INDEX = 4294967295
    MAX_DATA_PER_EDGE = 4
    MAX_DATA_PER_FACE = 4


class EdgeFlagBits(Enum):
    EDGE_SILHOUETTE = 1
    EDGE_RETRIANGULATED = 2
    EDGE_ORIGINAL = 4
    OPPOSITE_EDGE_UNLOADED_UNUSED = 8
    EDGE_USER = 16
    EDGE_BLOCKED = 32
    EDGE_EXTERNAL_OPPOSITE = 64


class hkaiNavMesh(hkReferencedObject):
    faces: hkaiNavMeshFace
    edges: hkaiNavMeshEdge
    vertices: any
    streamingSets: hkaiStreamingSet
    faceData: any
    edgeData: any
    faceDataStriding: int
    edgeDataStriding: int
    flags: int
    aabb: hkAabb
    erosionRadius: float
    userData: int
