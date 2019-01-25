import struct
from .hkpShapeKeyTableBlock import hkpShapeKeyTableBlock


class hkpShapeKeyTableBlock(object):
    slots: int
    next: any

    def __init__(self, infile):
        self.slots = struct.unpack('>I', infile.read(4))  # TYPE_UINT32:TYPE_VOID
        self.next = any(infile)  # TYPE_POINTER:TYPE_STRUCT

    def __repr__(self):
        return "<{class_name} slots={slots}, next={next}>".format(**{
            "class_name": self.__class__.__name__,
            "slots": self.slots,
            "next": self.next,
        })
