from .hkAabbHalf import hkAabbHalf
import struct


class hkcdDynamicTreeCodec18(object):
    aabb: hkAabbHalf
    parent: int

    def __init__(self, infile):
        self.aabb = hkAabbHalf(infile)  # TYPE_STRUCT:TYPE_VOID
        self.parent = struct.unpack('>H', infile.read(2))  # TYPE_UINT16:TYPE_VOID

    def __repr__(self):
        return "<{class_name} aabb={aabb}, parent={parent}>".format(**{
            "class_name": self.__class__.__name__,
            "aabb": self.aabb,
            "parent": self.parent,
        })
