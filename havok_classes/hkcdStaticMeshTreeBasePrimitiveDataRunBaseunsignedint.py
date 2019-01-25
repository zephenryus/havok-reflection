import struct


class hkcdStaticMeshTreeBasePrimitiveDataRunBaseunsignedint(object):
    value: int
    index: int
    count: int

    def __init__(self, infile):
        self.value = struct.unpack('>I', infile.read(4))
        self.index = struct.unpack('>B', infile.read(1))
        self.count = struct.unpack('>B', infile.read(1))
