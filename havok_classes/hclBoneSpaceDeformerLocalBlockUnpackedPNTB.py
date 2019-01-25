from .common import vector4
import struct


class hclBoneSpaceDeformerLocalBlockUnpackedPNTB(object):
    localPosition: vector4
    localNormal: vector4
    localTangent: vector4
    localBiTangent: vector4

    def __init__(self, infile):
        self.localPosition = struct.unpack('>4f', infile.read(16))
        self.localNormal = struct.unpack('>4f', infile.read(16))
        self.localTangent = struct.unpack('>4f', infile.read(16))
        self.localBiTangent = struct.unpack('>4f', infile.read(16))
