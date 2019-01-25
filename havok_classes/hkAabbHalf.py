import struct


class hkAabbHalf(object):
    data: int

    def __init__(self, infile):
        self.data = struct.unpack('>H', infile.read(2))  # TYPE_UINT16:TYPE_VOID

    def __repr__(self):
        return "<{class_name} data={data}>".format(**{
            "class_name": self.__class__.__name__,
            "data": self.data,
        })
