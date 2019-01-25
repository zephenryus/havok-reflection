from .common import vector4
import struct


class hclBoneSpaceDeformerLocalBlockUnpackedP(object):
    localPosition: vector4

    def __init__(self, infile):
        self.localPosition = struct.unpack('>4f', infile.read(16))
