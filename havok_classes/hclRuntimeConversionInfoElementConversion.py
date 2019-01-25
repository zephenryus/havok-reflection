import struct
from .enums import VectorConversion


class hclRuntimeConversionInfoElementConversion(object):
    index: int
    offset: int
    conversion: VectorConversion

    def __init__(self, infile):
        self.index = struct.unpack('>B', infile.read(1))
        self.offset = struct.unpack('>B', infile.read(1))
        self.conversion = VectorConversion(infile)  # TYPE_ENUM
