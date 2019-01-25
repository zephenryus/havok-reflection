import struct


class hkpSimpleMeshShapeTriangle(object):
    a: int
    b: int
    c: int
    weldingInfo: int

    def __init__(self, infile):
        self.a = struct.unpack('>i', infile.read(4))  # TYPE_INT32:TYPE_VOID
        self.b = struct.unpack('>i', infile.read(4))  # TYPE_INT32:TYPE_VOID
        self.c = struct.unpack('>i', infile.read(4))  # TYPE_INT32:TYPE_VOID
        self.weldingInfo = struct.unpack('>H', infile.read(2))  # TYPE_UINT16:TYPE_VOID

    def __repr__(self):
        return "<{class_name} a={a}, b={b}, c={c}, weldingInfo={weldingInfo}>".format(**{
            "class_name": self.__class__.__name__,
            "a": self.a,
            "b": self.b,
            "c": self.c,
            "weldingInfo": self.weldingInfo,
        })
