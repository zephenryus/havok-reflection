import struct


class hkpBreakableMultiMaterialInverseMappingDescriptor(object):
    offset: int
    numKeys: int

    def __init__(self, infile):
        self.offset = struct.unpack('>H', infile.read(2))
        self.numKeys = struct.unpack('>H', infile.read(2))
