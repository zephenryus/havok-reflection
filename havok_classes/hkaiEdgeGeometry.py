from .hkReferencedObject import hkReferencedObject
from enum import Enum
from typing import List
from .common import get_array
from .hkaiEdgeGeometryEdge import hkaiEdgeGeometryEdge
from .hkaiEdgeGeometryFace import hkaiEdgeGeometryFace


class FaceFlagBits(Enum):
    FLAGS_NONE = 0
    FLAGS_INPUT_GEOMETRY = 1
    FLAGS_PAINTER = 2
    FLAGS_CARVER = 4
    FLAGS_EXTRUDED = 8
    FLAGS_ALL = 15


class hkaiEdgeGeometry(hkReferencedObject):
    edges: List[hkaiEdgeGeometryEdge]
    faces: List[hkaiEdgeGeometryFace]
    vertices: List[vector4]
    zeroFace: hkaiEdgeGeometryFace

    def __init__(self, infile):
        self.edges = get_array(infile, hkaiEdgeGeometryEdge, 0)  # TYPE_ARRAY:TYPE_STRUCT
        self.faces = get_array(infile, hkaiEdgeGeometryFace, 0)  # TYPE_ARRAY:TYPE_STRUCT
        self.vertices = get_array(infile, vector4, 16)  # TYPE_ARRAY:TYPE_VECTOR4
        self.zeroFace = hkaiEdgeGeometryFace(infile)  # TYPE_STRUCT:TYPE_VOID

    def __repr__(self):
        return "<{class_name} edges=[{edges}], faces=[{faces}], vertices=[{vertices}], zeroFace={zeroFace}>".format(**{
            "class_name": self.__class__.__name__,
            "edges": self.edges,
            "faces": self.faces,
            "vertices": self.vertices,
            "zeroFace": self.zeroFace,
        })
