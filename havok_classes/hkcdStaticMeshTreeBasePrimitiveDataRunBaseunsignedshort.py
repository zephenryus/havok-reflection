import struct


class hkcdStaticMeshTreeBasePrimitiveDataRunBaseunsignedshort(object):
    value: int
    index: int
    count: int

    def __init__(self, infile):
        self.value = struct.unpack('>H', infile.read(2))  # TYPE_UINT16:TYPE_VOID
        self.index = struct.unpack('>B', infile.read(1))  # TYPE_UINT8:TYPE_VOID
        self.count = struct.unpack('>B', infile.read(1))  # TYPE_UINT8:TYPE_VOID

    def __repr__(self):
        return "<{class_name} value={value}, index={index}, count={count}>".format(**{
            "class_name": self.__class__.__name__,
            "value": self.value,
            "index": self.index,
            "count": self.count,
        })
