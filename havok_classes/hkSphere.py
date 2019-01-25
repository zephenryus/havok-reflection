from .common import vector4
import struct


class hkSphere(object):
    pos: vector4

    def __init__(self, infile):
        self.pos = struct.unpack('>4f', infile.read(16))
