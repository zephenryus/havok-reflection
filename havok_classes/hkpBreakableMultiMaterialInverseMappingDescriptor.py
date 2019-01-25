import struct


class hkpBreakableMultiMaterialInverseMappingDescriptor(object):
    offset: int
    numKeys: int

    def __init__(self, infile):
        self.offset = struct.unpack('>H', infile.read(2))  # TYPE_UINT16:TYPE_VOID
        self.numKeys = struct.unpack('>H', infile.read(2))  # TYPE_UINT16:TYPE_VOID

    def __repr__(self):
        return "<{class_name} offset={offset}, numKeys={numKeys}>".format(**{
            "class_name": self.__class__.__name__,
            "offset": self.offset,
            "numKeys": self.numKeys,
        })
