from .common import vector4
import struct


class hkpMoppCodeCodeInfo(object):
    offset: vector4

    def __init__(self, infile):
        self.offset = struct.unpack('>4f', infile.read(16))
