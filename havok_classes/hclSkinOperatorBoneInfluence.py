import struct


class hclSkinOperatorBoneInfluence(object):
    boneIndex: int
    weight: int

    def __init__(self, infile):
        self.boneIndex = struct.unpack('>B', infile.read(1))
        self.weight = struct.unpack('>B', infile.read(1))
