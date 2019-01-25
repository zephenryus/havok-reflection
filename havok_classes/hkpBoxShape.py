from .hkpConvexShape import hkpConvexShape
from .common import vector4
import struct


class hkpBoxShape(hkpConvexShape):
    halfExtents: vector4

    def __init__(self, infile):
        self.halfExtents = struct.unpack('>4f', infile.read(16))
