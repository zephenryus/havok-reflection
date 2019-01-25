import struct


class hclSimpleMeshBoneDeformOperatorTriangleBonePair(object):
    boneOffset: int
    triangleOffset: int

    def __init__(self, infile):
        self.boneOffset = struct.unpack('>H', infile.read(2))
        self.triangleOffset = struct.unpack('>H', infile.read(2))
