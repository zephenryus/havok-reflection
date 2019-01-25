from .hkReferencedObject import hkReferencedObject
from enum import Enum
from .common import any
from .hkGeometryTriangle import hkGeometryTriangle


class GeometryType(Enum):
    GEOMETRY_STATIC = 0
    GEOMETRY_DYNAMIC_VERTICES = 1


class hkGeometry(hkReferencedObject):
    vertices: any
    triangles: hkGeometryTriangle

    def __init__(self, infile):
        self.vertices = any(infile)  # TYPE_ARRAY
        self.triangles = hkGeometryTriangle(infile)  # TYPE_ARRAY
