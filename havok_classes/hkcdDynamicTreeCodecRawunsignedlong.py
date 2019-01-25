from .hkAabb import hkAabb
import struct


class hkcdDynamicTreeCodecRawunsignedlong(object):
    aabb: hkAabb
    parent: int
    children: int

    def __init__(self, infile):
        self.aabb = hkAabb(infile)  # TYPE_STRUCT:TYPE_VOID
        self.parent = struct.unpack('>L', infile.read(8))  # TYPE_ULONG:TYPE_VOID
        self.children = struct.unpack('>L', infile.read(8))  # TYPE_ULONG:TYPE_VOID

    def __repr__(self):
        return "<{class_name} aabb={aabb}, parent={parent}, children={children}>".format(**{
            "class_name": self.__class__.__name__,
            "aabb": self.aabb,
            "parent": self.parent,
            "children": self.children,
        })
