import struct


class hkFloat16(object):
    value: int

    def __init__(self, infile):
        self.value = struct.unpack('>H', infile.read(2))  # TYPE_UINT16:TYPE_VOID

    def __repr__(self):
        return "<{class_name} value={value}>".format(**{
            "class_name": self.__class__.__name__,
            "value": self.value,
        })
