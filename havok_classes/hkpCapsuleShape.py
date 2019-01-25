from .hkpConvexShape import hkpConvexShape
from enum import Enum
import struct


class RayHitType(Enum):
    HIT_CAP0 = 0
    HIT_CAP1 = 1
    HIT_BODY = 2


class hkpCapsuleShape(hkpConvexShape):
    vertexA: vector4
    vertexB: vector4

    def __init__(self, infile):
        self.vertexA = struct.unpack('>4f', infile.read(16))  # TYPE_VECTOR4:TYPE_VOID
        self.vertexB = struct.unpack('>4f', infile.read(16))  # TYPE_VECTOR4:TYPE_VOID

    def __repr__(self):
        return "<{class_name} vertexA={vertexA}, vertexB={vertexB}>".format(**{
            "class_name": self.__class__.__name__,
            "vertexA": self.vertexA,
            "vertexB": self.vertexB,
        })
