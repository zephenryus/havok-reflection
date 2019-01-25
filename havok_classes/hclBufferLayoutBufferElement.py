from .enums import VectorConversion
import struct


class hclBufferLayoutBufferElement(object):
    vectorConversion: VectorConversion
    vectorSize: int
    slotId: int
    slotStart: int

    def __init__(self, infile):
        self.vectorConversion = VectorConversion(infile)  # TYPE_ENUM
        self.vectorSize = struct.unpack('>B', infile.read(1))
        self.slotId = struct.unpack('>B', infile.read(1))
        self.slotStart = struct.unpack('>B', infile.read(1))
