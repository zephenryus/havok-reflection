import struct


class hclRuntimeConversionInfoSlotConversion(object):
    elements: int
    numElements: int
    index: int
    partialWrite: bool

    def __init__(self, infile):
        self.elements = struct.unpack('>B', infile.read(1))  # TYPE_UINT8:TYPE_VOID
        self.numElements = struct.unpack('>B', infile.read(1))  # TYPE_UINT8:TYPE_VOID
        self.index = struct.unpack('>B', infile.read(1))  # TYPE_UINT8:TYPE_VOID
        self.partialWrite = struct.unpack('>?', infile.read(1))  # TYPE_BOOL:TYPE_VOID

    def __repr__(self):
        return "<{class_name} elements={elements}, numElements={numElements}, index={index}, partialWrite={partialWrite}>".format(**{
            "class_name": self.__class__.__name__,
            "elements": self.elements,
            "numElements": self.numElements,
            "index": self.index,
            "partialWrite": self.partialWrite,
        })
