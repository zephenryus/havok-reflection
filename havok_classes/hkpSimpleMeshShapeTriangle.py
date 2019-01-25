import struct


class hkpSimpleMeshShapeTriangle(object):
    a: int
    b: int
    c: int
    weldingInfo: int

    def __init__(self, infile):
        self.a = struct.unpack('>i', infile.read(4))
        self.b = struct.unpack('>i', infile.read(4))
        self.c = struct.unpack('>i', infile.read(4))
        self.weldingInfo = struct.unpack('>H', infile.read(2))
