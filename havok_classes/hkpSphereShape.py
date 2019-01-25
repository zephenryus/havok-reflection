from .hkpConvexShape import hkpConvexShape
import struct


class hkpSphereShape(hkpConvexShape):
    pad16: int

    def __init__(self, infile):
        self.pad16 = struct.unpack('>I', infile.read(4))
