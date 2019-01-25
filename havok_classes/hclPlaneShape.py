from .hclShape import hclShape
import struct


class hclPlaneShape(hclShape):
    planeEquation: vector4

    def __init__(self, infile):
        self.planeEquation = struct.unpack('>4f', infile.read(16))  # TYPE_VECTOR4:TYPE_VOID

    def __repr__(self):
        return "<{class_name} planeEquation={planeEquation}>".format(**{
            "class_name": self.__class__.__name__,
            "planeEquation": self.planeEquation,
        })
