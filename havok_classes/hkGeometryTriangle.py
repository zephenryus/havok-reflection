import struct


class hkGeometryTriangle(object):
    a: int
    b: int
    c: int
    material: int

    def __init__(self, infile):
        self.a = struct.unpack('>i', infile.read(4))
        self.b = struct.unpack('>i', infile.read(4))
        self.c = struct.unpack('>i', infile.read(4))
        self.material = struct.unpack('>i', infile.read(4))
