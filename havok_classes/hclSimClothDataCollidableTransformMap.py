import struct
from .common import any


class hclSimClothDataCollidableTransformMap(object):
    transformSetIndex: int
    transformIndices: any
    offsets: any

    def __init__(self, infile):
        self.transformSetIndex = struct.unpack('>i', infile.read(4))
        self.transformIndices = any(infile)  # TYPE_ARRAY
        self.offsets = any(infile)  # TYPE_ARRAY
