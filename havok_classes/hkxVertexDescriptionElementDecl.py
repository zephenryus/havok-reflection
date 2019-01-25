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
        self.byteOffset = struct.unpack('>I', infile.read(4))  # TYPE_UINT32:TYPE_VOID
        self.type = DataType(infile)  # TYPE_ENUM:TYPE_UINT16
        self.usage = DataUsage(infile)  # TYPE_ENUM:TYPE_UINT16
        self.byteStride = struct.unpack('>I', infile.read(4))  # TYPE_UINT32:TYPE_VOID
        self.numElements = struct.unpack('>B', infile.read(1))  # TYPE_UINT8:TYPE_VOID
        self.channelID = struct.unpack('>s', infile.read(0))  # TYPE_STRINGPTR:TYPE_VOID

    def __repr__(self):
        return "<{class_name} byteOffset={byteOffset}, type={type}, usage={usage}, byteStride={byteStride}, numElements={numElements}, channelID=\"{channelID}\">".format(**{
            "class_name": self.__class__.__name__,
            "byteOffset": self.byteOffset,
            "type": self.type,
            "usage": self.usage,
            "byteStride": self.byteStride,
            "numElements": self.numElements,
            "channelID": self.channelID,
        })
