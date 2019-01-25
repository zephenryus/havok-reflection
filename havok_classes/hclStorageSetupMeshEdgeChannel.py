from .enums import EdgeChannelType


class hclStorageSetupMeshEdgeChannel(object):
    name: str
    type: EdgeChannelType

    def __init__(self, infile):
        self.name = struct.unpack('>s', infile.read(0))
        self.type = EdgeChannelType(infile)  # TYPE_ENUM
