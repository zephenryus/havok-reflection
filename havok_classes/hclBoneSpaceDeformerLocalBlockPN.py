from .common import vector4
import struct


class hclBoneSpaceDeformerLocalBlockPN(object):
    localPosition: vector4
    localNormal: int

    def __init__(self, infile):
        self.localPosition = struct.unpack('>4f', infile.read(16))
        self.localNormal = struct.unpack('>h', infile.read(2))
