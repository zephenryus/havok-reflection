from .hkpConvexShape import hkpConvexShape
import struct


class hkpBoxShape(hkpConvexShape):
    halfExtents: vector4

    def __init__(self, infile):
        self.halfExtents = struct.unpack('>4f', infile.read(16))  # TYPE_VECTOR4:TYPE_VOID

    def __repr__(self):
        return "<{class_name} halfExtents={halfExtents}>".format(**{
            "class_name": self.__class__.__name__,
            "halfExtents": self.halfExtents,
        })
