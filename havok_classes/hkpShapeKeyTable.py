from .hkpShapeKeyTableBlock import hkpShapeKeyTableBlock
import struct


class hkpShapeKeyTable(object):
    lists: any
    occupancyBitField: int

    def __init__(self, infile):
        self.lists = any(infile)  # TYPE_POINTER:TYPE_STRUCT
        self.occupancyBitField = struct.unpack('>I', infile.read(4))  # TYPE_UINT32:TYPE_VOID

    def __repr__(self):
        return "<{class_name} lists={lists}, occupancyBitField={occupancyBitField}>".format(**{
            "class_name": self.__class__.__name__,
            "lists": self.lists,
            "occupancyBitField": self.occupancyBitField,
        })
