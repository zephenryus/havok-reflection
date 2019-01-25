import struct
from .hkpShapeKeyTableBlock import hkpShapeKeyTableBlock


class hkpShapeKeyTableBlock(object):
    slots: int
    next: hkpShapeKeyTableBlock

    def __init__(self, infile):
        self.slots = struct.unpack('>I', infile.read(4))
        self.next = hkpShapeKeyTableBlock(infile)  # TYPE_POINTER
