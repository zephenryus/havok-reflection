import struct


class hkFourTransposedPointsf(object):
    vertices: vector4

    def __init__(self, infile):
        self.vertices = struct.unpack('>4f', infile.read(16))  # TYPE_VECTOR4:TYPE_VOID

    def __repr__(self):
        return "<{class_name} vertices={vertices}>".format(**{
            "class_name": self.__class__.__name__,
            "vertices": self.vertices,
        })
