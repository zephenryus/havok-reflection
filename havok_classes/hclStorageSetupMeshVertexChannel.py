from .enums import VertexChannelType


class hclStorageSetupMeshVertexChannel(object):
    name: str
    type: VertexChannelType

    def __init__(self, infile):
        self.name = struct.unpack('>s', infile.read(0))
        self.type = VertexChannelType(infile)  # TYPE_ENUM
