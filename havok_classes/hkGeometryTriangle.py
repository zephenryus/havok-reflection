import struct


class hkGeometryTriangle(object):
    a: int
    b: int
    c: int
    material: int

    def __init__(self, infile):
        self.a = struct.unpack('>i', infile.read(4))  # TYPE_INT32:TYPE_VOID
        self.b = struct.unpack('>i', infile.read(4))  # TYPE_INT32:TYPE_VOID
        self.c = struct.unpack('>i', infile.read(4))  # TYPE_INT32:TYPE_VOID
        self.material = struct.unpack('>i', infile.read(4))  # TYPE_INT32:TYPE_VOID

    def __repr__(self):
        return "<{class_name} a={a}, b={b}, c={c}, material={material}>".format(**{
            "class_name": self.__class__.__name__,
            "a": self.a,
            "b": self.b,
            "c": self.c,
            "material": self.material,
        })
