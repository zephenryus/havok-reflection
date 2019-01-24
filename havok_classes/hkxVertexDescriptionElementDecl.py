from .enums import DataType, DataUsage


class hkxVertexDescriptionElementDecl(object):
    byteOffset: int
    type: DataType
    usage: DataUsage
    byteStride: int
    numElements: int
    channelID: str
