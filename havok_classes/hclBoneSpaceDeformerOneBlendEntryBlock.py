import struct


class hclBoneSpaceDeformerOneBlendEntryBlock(object):
    vertexIndices: int
    boneIndices: int

    def __init__(self, infile):
        self.vertexIndices = struct.unpack('>H', infile.read(2))
        self.boneIndices = struct.unpack('>H', infile.read(2))
