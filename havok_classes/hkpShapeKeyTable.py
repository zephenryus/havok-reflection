from .hkpShapeKeyTableBlock import hkpShapeKeyTableBlock
import struct


class hkpShapeKeyTable(object):
    lists: hkpShapeKeyTableBlock
    occupancyBitField: int

    def __init__(self, infile):
        self.lists = hkpShapeKeyTableBlock(infile)  # TYPE_POINTER
        self.occupancyBitField = struct.unpack('>I', infile.read(4))
