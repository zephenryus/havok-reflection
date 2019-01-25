from .hkpConvexShape import hkpConvexShape
from enum import Enum
import struct


class VertexIdEncoding(Enum):
    VERTEX_ID_ENCODING_IS_BASE_A_SHIFT = 7
    VERTEX_ID_ENCODING_SIN_SIGN_SHIFT = 6
    VERTEX_ID_ENCODING_COS_SIGN_SHIFT = 5
    VERTEX_ID_ENCODING_IS_SIN_LESSER_SHIFT = 4
    VERTEX_ID_ENCODING_VALUE_MASK = 15


class hkpCylinderShape(hkpConvexShape):
    cylRadius: float
    cylBaseRadiusFactorForHeightFieldCollisions: float
    vertexA: vector4
    vertexB: vector4
    perpendicular1: vector4
    perpendicular2: vector4

    def __init__(self, infile):
        self.cylRadius = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.cylBaseRadiusFactorForHeightFieldCollisions = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.vertexA = struct.unpack('>4f', infile.read(16))  # TYPE_VECTOR4:TYPE_VOID
        self.vertexB = struct.unpack('>4f', infile.read(16))  # TYPE_VECTOR4:TYPE_VOID
        self.perpendicular1 = struct.unpack('>4f', infile.read(16))  # TYPE_VECTOR4:TYPE_VOID
        self.perpendicular2 = struct.unpack('>4f', infile.read(16))  # TYPE_VECTOR4:TYPE_VOID

    def __repr__(self):
        return "<{class_name} cylRadius={cylRadius}, cylBaseRadiusFactorForHeightFieldCollisions={cylBaseRadiusFactorForHeightFieldCollisions}, vertexA={vertexA}, vertexB={vertexB}, perpendicular1={perpendicular1}, perpendicular2={perpendicular2}>".format(**{
            "class_name": self.__class__.__name__,
            "cylRadius": self.cylRadius,
            "cylBaseRadiusFactorForHeightFieldCollisions": self.cylBaseRadiusFactorForHeightFieldCollisions,
            "vertexA": self.vertexA,
            "vertexB": self.vertexB,
            "perpendicular1": self.perpendicular1,
            "perpendicular2": self.perpendicular2,
        })
