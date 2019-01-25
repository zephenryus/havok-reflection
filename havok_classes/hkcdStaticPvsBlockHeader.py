import struct


class hkcdStaticPvsBlockHeader(object):
    offset: int
    length: int

    def __init__(self, infile):
        self.offset = struct.unpack('>I', infile.read(4))  # TYPE_UINT32:TYPE_VOID
        self.length = struct.unpack('>I', infile.read(4))  # TYPE_UINT32:TYPE_VOID

    def __repr__(self):
        return "<{class_name} offset={offset}, length={length}>".format(**{
            "class_name": self.__class__.__name__,
            "offset": self.offset,
            "length": self.length,
        })
