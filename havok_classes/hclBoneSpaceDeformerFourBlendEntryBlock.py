import struct


class hclBoneSpaceDeformerFourBlendEntryBlock(object):
    vertexIndices: int
    boneIndices: int
    padding: int

    def __init__(self, infile):
        self.vertexIndices = struct.unpack('>H', infile.read(2))
        self.boneIndices = struct.unpack('>H', infile.read(2))
        self.padding = struct.unpack('>B', infile.read(1))
