import struct
from .common import any


class hkaiEdgeGeometryFace(object):
    data: int
    faceIndex: int
    flags: any

    def __init__(self, infile):
        self.data = struct.unpack('>I', infile.read(4))
        self.faceIndex = struct.unpack('>I', infile.read(4))
        self.flags = any(infile)  # TYPE_FLAGS
