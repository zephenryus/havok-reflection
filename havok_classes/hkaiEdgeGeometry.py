from .hkReferencedObject import hkReferencedObject
from enum import Enum
from .hkaiEdgeGeometryEdge import hkaiEdgeGeometryEdge
from .hkaiEdgeGeometryFace import hkaiEdgeGeometryFace
from .common import any


class FaceFlagBits(Enum):
    FLAGS_NONE = 0
    FLAGS_INPUT_GEOMETRY = 1
    FLAGS_PAINTER = 2
    FLAGS_CARVER = 4
    FLAGS_EXTRUDED = 8
    FLAGS_ALL = 15


class hkaiEdgeGeometry(hkReferencedObject):
    edges: hkaiEdgeGeometryEdge
    faces: hkaiEdgeGeometryFace
    vertices: any
    zeroFace: hkaiEdgeGeometryFace

    def __init__(self, infile):
        self.edges = hkaiEdgeGeometryEdge(infile)  # TYPE_ARRAY
        self.faces = hkaiEdgeGeometryFace(infile)  # TYPE_ARRAY
        self.vertices = any(infile)  # TYPE_ARRAY
        self.zeroFace = hkaiEdgeGeometryFace(infile)  # TYPE_STRUCT
