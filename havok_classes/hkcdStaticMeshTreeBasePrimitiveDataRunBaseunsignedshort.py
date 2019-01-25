import struct


class hkcdStaticMeshTreeBasePrimitiveDataRunBaseunsignedshort(object):
    value: int
    index: int
    count: int

    def __init__(self, infile):
        self.value = struct.unpack('>H', infile.read(2))
        self.index = struct.unpack('>B', infile.read(1))
        self.count = struct.unpack('>B', infile.read(1))
