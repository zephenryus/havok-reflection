import struct


class hkIntRealPair(object):
    key: int
    value: float

    def __init__(self, infile):
        self.key = struct.unpack('>i', infile.read(4))  # TYPE_INT32:TYPE_VOID
        self.value = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID

    def __repr__(self):
        return "<{class_name} key={key}, value={value}>".format(**{
            "class_name": self.__class__.__name__,
            "key": self.key,
            "value": self.value,
        })
