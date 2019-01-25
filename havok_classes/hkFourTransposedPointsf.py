from .common import vector4
import struct


class hkFourTransposedPointsf(object):
    vertices: vector4

    def __init__(self, infile):
        self.vertices = struct.unpack('>4f', infile.read(16))
