import struct


class hclBoneSpaceDeformerFourBlendEntryBlock(object):
    vertexIndices: int
    boneIndices: int
    padding: int

    def __init__(self, infile):
        self.vertexIndices = struct.unpack('>H', infile.read(2))  # TYPE_UINT16:TYPE_VOID
        self.boneIndices = struct.unpack('>H', infile.read(2))  # TYPE_UINT16:TYPE_VOID
        self.padding = struct.unpack('>B', infile.read(1))  # TYPE_UINT8:TYPE_VOID

    def __repr__(self):
        return "<{class_name} vertexIndices={vertexIndices}, boneIndices={boneIndices}, padding={padding}>".format(**{
            "class_name": self.__class__.__name__,
            "vertexIndices": self.vertexIndices,
            "boneIndices": self.boneIndices,
            "padding": self.padding,
        })
