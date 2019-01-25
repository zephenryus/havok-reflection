from .hkReferencedObject import hkReferencedObject
from enum import Enum
from typing import List
from .common import get_array
from .hkGeometryTriangle import hkGeometryTriangle


class GeometryType(Enum):
    GEOMETRY_STATIC = 0
    GEOMETRY_DYNAMIC_VERTICES = 1


class hkGeometry(hkReferencedObject):
    vertices: List[vector4]
    triangles: List[hkGeometryTriangle]

    def __init__(self, infile):
        self.vertices = get_array(infile, vector4, 16)  # TYPE_ARRAY:TYPE_VECTOR4
        self.triangles = get_array(infile, hkGeometryTriangle, 0)  # TYPE_ARRAY:TYPE_STRUCT

    def __repr__(self):
        return "<{class_name} vertices=[{vertices}], triangles=[{triangles}]>".format(**{
            "class_name": self.__class__.__name__,
            "vertices": self.vertices,
            "triangles": self.triangles,
        })
