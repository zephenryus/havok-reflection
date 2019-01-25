from .hkpShapeCollection import hkpShapeCollection
from typing import List
from .common import get_array
from .hkpSimpleMeshShapeTriangle import hkpSimpleMeshShapeTriangle
import struct
from .enums import WeldingType


class hkpSimpleMeshShape(hkpShapeCollection):
    vertices: List[vector4]
    triangles: List[hkpSimpleMeshShapeTriangle]
    materialIndices: List[int]
    radius: float
    weldingType: WeldingType

    def __init__(self, infile):
        self.vertices = get_array(infile, vector4, 16)  # TYPE_ARRAY:TYPE_VECTOR4
        self.triangles = get_array(infile, hkpSimpleMeshShapeTriangle, 0)  # TYPE_ARRAY:TYPE_STRUCT
        self.materialIndices = get_array(infile, int, 1)  # TYPE_ARRAY:TYPE_UINT8
        self.radius = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.weldingType = WeldingType(infile)  # TYPE_ENUM:TYPE_UINT8

    def __repr__(self):
        return "<{class_name} vertices=[{vertices}], triangles=[{triangles}], materialIndices=[{materialIndices}], radius={radius}, weldingType={weldingType}>".format(**{
            "class_name": self.__class__.__name__,
            "vertices": self.vertices,
            "triangles": self.triangles,
            "materialIndices": self.materialIndices,
            "radius": self.radius,
            "weldingType": self.weldingType,
        })
