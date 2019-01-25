import struct


class hkpMoppCodeCodeInfo(object):
    offset: vector4

    def __init__(self, infile):
        self.offset = struct.unpack('>4f', infile.read(16))  # TYPE_VECTOR4:TYPE_VOID

    def __repr__(self):
        return "<{class_name} offset={offset}>".format(**{
            "class_name": self.__class__.__name__,
            "offset": self.offset,
        })
