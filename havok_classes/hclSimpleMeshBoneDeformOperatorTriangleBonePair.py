import struct


class hclSimpleMeshBoneDeformOperatorTriangleBonePair(object):
    boneOffset: int
    triangleOffset: int

    def __init__(self, infile):
        self.boneOffset = struct.unpack('>H', infile.read(2))  # TYPE_UINT16:TYPE_VOID
        self.triangleOffset = struct.unpack('>H', infile.read(2))  # TYPE_UINT16:TYPE_VOID

    def __repr__(self):
        return "<{class_name} boneOffset={boneOffset}, triangleOffset={triangleOffset}>".format(**{
            "class_name": self.__class__.__name__,
            "boneOffset": self.boneOffset,
            "triangleOffset": self.triangleOffset,
        })
