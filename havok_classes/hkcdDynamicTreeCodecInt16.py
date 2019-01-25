from .hkcdDynamicTreeCodecInt16IntAabb import hkcdDynamicTreeCodecInt16IntAabb
import struct


class hkcdDynamicTreeCodecInt16(object):
    aabb: hkcdDynamicTreeCodecInt16IntAabb
    parent: int
    children: int
    pad: int

    def __init__(self, infile):
        self.aabb = hkcdDynamicTreeCodecInt16IntAabb(infile)  # TYPE_STRUCT:TYPE_VOID
        self.parent = struct.unpack('>I', infile.read(4))  # TYPE_UINT32:TYPE_VOID
        self.children = struct.unpack('>I', infile.read(4))  # TYPE_UINT32:TYPE_VOID
        self.pad = struct.unpack('>I', infile.read(4))  # TYPE_UINT32:TYPE_VOID

    def __repr__(self):
        return "<{class_name} aabb={aabb}, parent={parent}, children={children}, pad={pad}>".format(**{
            "class_name": self.__class__.__name__,
            "aabb": self.aabb,
            "parent": self.parent,
            "children": self.children,
            "pad": self.pad,
        })
