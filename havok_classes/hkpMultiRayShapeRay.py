from .common import vector4
import struct


class hkpMultiRayShapeRay(object):
    start: vector4
    end: vector4

    def __init__(self, infile):
        self.start = struct.unpack('>4f', infile.read(16))
        self.end = struct.unpack('>4f', infile.read(16))
