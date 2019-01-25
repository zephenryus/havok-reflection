from .enums import TriangleChannelType


class hclStorageSetupMeshTriangleChannel(object):
    name: str
    type: TriangleChannelType

    def __init__(self, infile):
        self.name = struct.unpack('>s', infile.read(0))  # TYPE_STRINGPTR:TYPE_VOID
        self.type = TriangleChannelType(infile)  # TYPE_ENUM:TYPE_UINT32

    def __repr__(self):
        return "<{class_name} name=\"{name}\", type={type}>".format(**{
            "class_name": self.__class__.__name__,
            "name": self.name,
            "type": self.type,
        })
