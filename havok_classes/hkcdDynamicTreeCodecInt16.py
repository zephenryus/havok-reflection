from .hkcdDynamicTreeCodecInt16IntAabb import hkcdDynamicTreeCodecInt16IntAabb
import struct


class hkcdDynamicTreeCodecInt16(object):
    aabb: hkcdDynamicTreeCodecInt16IntAabb
    parent: int
    children: int
    pad: int

    def __init__(self, infile):
        self.aabb = hkcdDynamicTreeCodecInt16IntAabb(infile)  # TYPE_STRUCT
        self.parent = struct.unpack('>I', infile.read(4))
        self.children = struct.unpack('>I', infile.read(4))
        self.pad = struct.unpack('>I', infile.read(4))
