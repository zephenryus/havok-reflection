from .enums import TriangleChannelType


class hclStorageSetupMeshTriangleChannel(object):
    name: str
    type: TriangleChannelType

    def __init__(self, infile):
        self.name = struct.unpack('>s', infile.read(0))
        self.type = TriangleChannelType(infile)  # TYPE_ENUM
