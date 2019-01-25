import struct


class hclSkinOperatorBoneInfluence(object):
    boneIndex: int
    weight: int

    def __init__(self, infile):
        self.boneIndex = struct.unpack('>B', infile.read(1))  # TYPE_UINT8:TYPE_VOID
        self.weight = struct.unpack('>B', infile.read(1))  # TYPE_UINT8:TYPE_VOID

    def __repr__(self):
        return "<{class_name} boneIndex={boneIndex}, weight={weight}>".format(**{
            "class_name": self.__class__.__name__,
            "boneIndex": self.boneIndex,
            "weight": self.weight,
        })
