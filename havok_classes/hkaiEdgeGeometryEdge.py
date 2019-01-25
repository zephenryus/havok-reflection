import struct


class hkaiEdgeGeometryEdge(object):
    a: int
    b: int
    face: int
    data: int

    def __init__(self, infile):
        self.a = struct.unpack('>I', infile.read(4))  # TYPE_UINT32:TYPE_VOID
        self.b = struct.unpack('>I', infile.read(4))  # TYPE_UINT32:TYPE_VOID
        self.face = struct.unpack('>I', infile.read(4))  # TYPE_UINT32:TYPE_VOID
        self.data = struct.unpack('>I', infile.read(4))  # TYPE_UINT32:TYPE_VOID

    def __repr__(self):
        return "<{class_name} a={a}, b={b}, face={face}, data={data}>".format(**{
            "class_name": self.__class__.__name__,
            "a": self.a,
            "b": self.b,
            "face": self.face,
            "data": self.data,
        })
