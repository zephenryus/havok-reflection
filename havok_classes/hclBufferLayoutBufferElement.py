from .enums import VectorConversion
import struct


class hclBufferLayoutBufferElement(object):
    vectorConversion: VectorConversion
    vectorSize: int
    slotId: int
    slotStart: int

    def __init__(self, infile):
        self.vectorConversion = VectorConversion(infile)  # TYPE_ENUM:TYPE_UINT8
        self.vectorSize = struct.unpack('>B', infile.read(1))  # TYPE_UINT8:TYPE_VOID
        self.slotId = struct.unpack('>B', infile.read(1))  # TYPE_UINT8:TYPE_VOID
        self.slotStart = struct.unpack('>B', infile.read(1))  # TYPE_UINT8:TYPE_VOID

    def __repr__(self):
        return "<{class_name} vectorConversion={vectorConversion}, vectorSize={vectorSize}, slotId={slotId}, slotStart={slotStart}>".format(**{
            "class_name": self.__class__.__name__,
            "vectorConversion": self.vectorConversion,
            "vectorSize": self.vectorSize,
            "slotId": self.slotId,
            "slotStart": self.slotStart,
        })
