from .hkReferencedObject import hkReferencedObject
from enum import Enum
from .hkaiNavMeshFace import hkaiNavMeshFace
from .hkaiNavMeshEdge import hkaiNavMeshEdge
from .common import any
from .hkaiStreamingSet import hkaiStreamingSet
import struct
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

    def __init__(self, infile):
        self.faces = hkaiNavMeshFace(infile)  # TYPE_ARRAY
        self.edges = hkaiNavMeshEdge(infile)  # TYPE_ARRAY
        self.vertices = any(infile)  # TYPE_ARRAY
        self.streamingSets = hkaiStreamingSet(infile)  # TYPE_ARRAY
        self.faceData = any(infile)  # TYPE_ARRAY
        self.edgeData = any(infile)  # TYPE_ARRAY
        self.faceDataStriding = struct.unpack('>i', infile.read(4))
        self.edgeDataStriding = struct.unpack('>i', infile.read(4))
        self.flags = struct.unpack('>B', infile.read(1))
        self.aabb = hkAabb(infile)  # TYPE_STRUCT
        self.erosionRadius = struct.unpack('>f', infile.read(4))
        self.userData = struct.unpack('>L', infile.read(8))
