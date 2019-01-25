from .common import vector4
import struct


class hkAabb(object):
    min: vector4
    max: vector4

    def __init__(self, infile):
        self.min = struct.unpack('>4f', infile.read(16))
        self.max = struct.unpack('>4f', infile.read(16))
