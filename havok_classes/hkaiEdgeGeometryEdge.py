import struct


class hkaiEdgeGeometryEdge(object):
    a: int
    b: int
    face: int
    data: int

    def __init__(self, infile):
        self.a = struct.unpack('>I', infile.read(4))
        self.b = struct.unpack('>I', infile.read(4))
        self.face = struct.unpack('>I', infile.read(4))
        self.data = struct.unpack('>I', infile.read(4))
