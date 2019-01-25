from .common import vector4
import struct


class hkpTyremarkPoint(object):
    pointLeft: vector4
    pointRight: vector4

    def __init__(self, infile):
        self.pointLeft = struct.unpack('>4f', infile.read(16))
        self.pointRight = struct.unpack('>4f', infile.read(16))
