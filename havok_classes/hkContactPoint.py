from .common import vector4
import struct


class hkContactPoint(object):
    position: vector4
    separatingNormal: vector4

    def __init__(self, infile):
        self.position = struct.unpack('>4f', infile.read(16))
        self.separatingNormal = struct.unpack('>4f', infile.read(16))
