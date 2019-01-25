import struct


class hkpCompressedMeshShapeBigTriangle(object):
    a: int
    b: int
    c: int
    material: int
    weldingInfo: int
    transformIndex: int

    def __init__(self, infile):
        self.a = struct.unpack('>H', infile.read(2))  # TYPE_UINT16:TYPE_VOID
        self.b = struct.unpack('>H', infile.read(2))  # TYPE_UINT16:TYPE_VOID
        self.c = struct.unpack('>H', infile.read(2))  # TYPE_UINT16:TYPE_VOID
        self.material = struct.unpack('>I', infile.read(4))  # TYPE_UINT32:TYPE_VOID
        self.weldingInfo = struct.unpack('>H', infile.read(2))  # TYPE_UINT16:TYPE_VOID
        self.transformIndex = struct.unpack('>H', infile.read(2))  # TYPE_UINT16:TYPE_VOID

    def __repr__(self):
        return "<{class_name} a={a}, b={b}, c={c}, material={material}, weldingInfo={weldingInfo}, transformIndex={transformIndex}>".format(**{
            "class_name": self.__class__.__name__,
            "a": self.a,
            "b": self.b,
            "c": self.c,
            "material": self.material,
            "weldingInfo": self.weldingInfo,
            "transformIndex": self.transformIndex,
        })
