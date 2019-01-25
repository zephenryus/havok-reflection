import struct


class hkpConstraintInstanceSmallArraySerializeOverrideType(object):
    data: any
    size: int
    capacityAndFlags: int

    def __init__(self, infile):
        self.data = any(infile)  # TYPE_POINTER:TYPE_VOID
        self.size = struct.unpack('>H', infile.read(2))  # TYPE_UINT16:TYPE_VOID
        self.capacityAndFlags = struct.unpack('>H', infile.read(2))  # TYPE_UINT16:TYPE_VOID

    def __repr__(self):
        return "<{class_name} data={data}, size={size}, capacityAndFlags={capacityAndFlags}>".format(**{
            "class_name": self.__class__.__name__,
            "data": self.data,
            "size": self.size,
            "capacityAndFlags": self.capacityAndFlags,
        })
