import struct
from .enums import DataType, DataUsage


class hkxVertexDescriptionElementDecl(object):
    byteOffset: int
    type: DataType
    usage: DataUsage
    byteStride: int
    numElements: int
    channelID: str

    def __init__(self, infile):
        self.byteOffset = struct.unpack('>I', infile.read(4))
        self.type = DataType(infile)  # TYPE_ENUM
        self.usage = DataUsage(infile)  # TYPE_ENUM
        self.byteStride = struct.unpack('>I', infile.read(4))
        self.numElements = struct.unpack('>B', infile.read(1))
        self.channelID = struct.unpack('>s', infile.read(0))
