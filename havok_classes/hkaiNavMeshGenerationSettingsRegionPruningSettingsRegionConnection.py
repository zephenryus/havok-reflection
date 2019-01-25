import struct


class hkaiNavMeshGenerationSettingsRegionPruningSettingsRegionConnection(object):
    a: vector4
    b: vector4

    def __init__(self, infile):
        self.a = struct.unpack('>4f', infile.read(16))  # TYPE_VECTOR4:TYPE_VOID
        self.b = struct.unpack('>4f', infile.read(16))  # TYPE_VECTOR4:TYPE_VOID

    def __repr__(self):
        return "<{class_name} a={a}, b={b}>".format(**{
            "class_name": self.__class__.__name__,
            "a": self.a,
            "b": self.b,
        })
