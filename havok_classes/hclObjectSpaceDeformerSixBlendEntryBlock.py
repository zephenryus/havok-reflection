import struct


class hclObjectSpaceDeformerSixBlendEntryBlock(object):
    vertexIndices: int
    boneIndices: int
    boneWeights: int

    def __init__(self, infile):
        self.vertexIndices = struct.unpack('>H', infile.read(2))  # TYPE_UINT16:TYPE_VOID
        self.boneIndices = struct.unpack('>H', infile.read(2))  # TYPE_UINT16:TYPE_VOID
        self.boneWeights = struct.unpack('>H', infile.read(2))  # TYPE_UINT16:TYPE_VOID

    def __repr__(self):
        return "<{class_name} vertexIndices={vertexIndices}, boneIndices={boneIndices}, boneWeights={boneWeights}>".format(**{
            "class_name": self.__class__.__name__,
            "vertexIndices": self.vertexIndices,
            "boneIndices": self.boneIndices,
            "boneWeights": self.boneWeights,
        })
