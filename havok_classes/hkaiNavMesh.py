from .hkReferencedObject import hkReferencedObject
from enum import Enum
from typing import List
from .common import get_array
from .hkaiNavMeshFace import hkaiNavMeshFace
from .hkaiNavMeshEdge import hkaiNavMeshEdge
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
    faces: List[hkaiNavMeshFace]
    edges: List[hkaiNavMeshEdge]
    vertices: List[vector4]
    streamingSets: List[hkaiStreamingSet]
    faceData: List[int]
    edgeData: List[int]
    faceDataStriding: int
    edgeDataStriding: int
    flags: int
    aabb: hkAabb
    erosionRadius: float
    userData: int

    def __init__(self, infile):
        self.faces = get_array(infile, hkaiNavMeshFace, 0)  # TYPE_ARRAY:TYPE_STRUCT
        self.edges = get_array(infile, hkaiNavMeshEdge, 0)  # TYPE_ARRAY:TYPE_STRUCT
        self.vertices = get_array(infile, vector4, 16)  # TYPE_ARRAY:TYPE_VECTOR4
        self.streamingSets = get_array(infile, hkaiStreamingSet, 0)  # TYPE_ARRAY:TYPE_STRUCT
        self.faceData = get_array(infile, int, 4)  # TYPE_ARRAY:TYPE_INT32
        self.edgeData = get_array(infile, int, 4)  # TYPE_ARRAY:TYPE_INT32
        self.faceDataStriding = struct.unpack('>i', infile.read(4))  # TYPE_INT32:TYPE_VOID
        self.edgeDataStriding = struct.unpack('>i', infile.read(4))  # TYPE_INT32:TYPE_VOID
        self.flags = struct.unpack('>B', infile.read(1))  # TYPE_UINT8:TYPE_VOID
        self.aabb = hkAabb(infile)  # TYPE_STRUCT:TYPE_VOID
        self.erosionRadius = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.userData = struct.unpack('>L', infile.read(8))  # TYPE_ULONG:TYPE_VOID

    def __repr__(self):
        return "<{class_name} faces=[{faces}], edges=[{edges}], vertices=[{vertices}], streamingSets=[{streamingSets}], faceData=[{faceData}], edgeData=[{edgeData}], faceDataStriding={faceDataStriding}, edgeDataStriding={edgeDataStriding}, flags={flags}, aabb={aabb}, erosionRadius={erosionRadius}, userData={userData}>".format(**{
            "class_name": self.__class__.__name__,
            "faces": self.faces,
            "edges": self.edges,
            "vertices": self.vertices,
            "streamingSets": self.streamingSets,
            "faceData": self.faceData,
            "edgeData": self.edgeData,
            "faceDataStriding": self.faceDataStriding,
            "edgeDataStriding": self.edgeDataStriding,
            "flags": self.flags,
            "aabb": self.aabb,
            "erosionRadius": self.erosionRadius,
            "userData": self.userData,
        })
