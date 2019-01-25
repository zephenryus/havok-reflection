import struct


class hclRuntimeConversionInfoSlotConversion(object):
    elements: int
    numElements: int
    index: int
    partialWrite: bool

    def __init__(self, infile):
        self.elements = struct.unpack('>B', infile.read(1))
        self.numElements = struct.unpack('>B', infile.read(1))
        self.index = struct.unpack('>B', infile.read(1))
        self.partialWrite = struct.unpack('>?', infile.read(1))
