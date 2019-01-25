import struct


class hkSimplePropertyValue(object):
    data: int

    def __init__(self, infile):
        self.data = struct.unpack('>Q', infile.read(8))  # TYPE_UINT64:TYPE_VOID

    def __repr__(self):
        return "<{class_name} data={data}>".format(**{
            "class_name": self.__class__.__name__,
            "data": self.data,
        })
