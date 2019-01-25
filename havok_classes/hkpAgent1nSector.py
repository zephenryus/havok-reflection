import struct


class hkpAgent1nSector(object):
    bytesAllocated: int
    pad0: int
    pad1: int
    pad2: int
    data: int

    def __init__(self, infile):
        self.bytesAllocated = struct.unpack('>I', infile.read(4))
        self.pad0 = struct.unpack('>I', infile.read(4))
        self.pad1 = struct.unpack('>I', infile.read(4))
        self.pad2 = struct.unpack('>I', infile.read(4))
        self.data = struct.unpack('>B', infile.read(1))
