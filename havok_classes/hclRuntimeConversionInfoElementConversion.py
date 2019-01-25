import struct
from .enums import VectorConversion


class hclRuntimeConversionInfoElementConversion(object):
    index: int
    offset: int
    conversion: VectorConversion

    def __init__(self, infile):
        self.index = struct.unpack('>B', infile.read(1))  # TYPE_UINT8:TYPE_VOID
        self.offset = struct.unpack('>B', infile.read(1))  # TYPE_UINT8:TYPE_VOID
        self.conversion = VectorConversion(infile)  # TYPE_ENUM:TYPE_UINT8

    def __repr__(self):
        return "<{class_name} index={index}, offset={offset}, conversion={conversion}>".format(**{
            "class_name": self.__class__.__name__,
            "index": self.index,
            "offset": self.offset,
            "conversion": self.conversion,
        })
