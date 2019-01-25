import struct


class hkAabbUint32(object):
    min: int
    expansionMin: int
    expansionShift: int
    max: int
    expansionMax: int
    shapeKeyByte: int

    def __init__(self, infile):
        self.min = struct.unpack('>I', infile.read(4))
        self.expansionMin = struct.unpack('>B', infile.read(1))
        self.expansionShift = struct.unpack('>B', infile.read(1))
        self.max = struct.unpack('>I', infile.read(4))
        self.expansionMax = struct.unpack('>B', infile.read(1))
        self.shapeKeyByte = struct.unpack('>B', infile.read(1))
