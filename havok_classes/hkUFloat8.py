import struct


class hkUFloat8(object):
    value: int

    def __init__(self, infile):
        self.value = struct.unpack('>B', infile.read(1))  # TYPE_UINT8:TYPE_VOID

    def __repr__(self):
        return "<{class_name} value={value}>".format(**{
            "class_name": self.__class__.__name__,
            "value": self.value,
        })
