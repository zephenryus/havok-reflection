import struct


class hkcdPlanarGeometryPrimitivesPlane(object):
    iEqn: int
    dEqn: int

    def __init__(self, infile):
        self.iEqn = struct.unpack('>q', infile.read(8))
        self.dEqn = struct.unpack('>q', infile.read(8))
