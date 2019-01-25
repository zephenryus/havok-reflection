from .common import any, vector4
import struct


class hkaiUserEdgeUtilsObb(object):
    transform: any
    halfExtents: vector4

    def __init__(self, infile):
        self.transform = any(infile)  # TYPE_TRANSFORM
        self.halfExtents = struct.unpack('>4f', infile.read(16))
