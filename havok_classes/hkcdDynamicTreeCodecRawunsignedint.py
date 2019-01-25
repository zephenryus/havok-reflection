from .hkAabb import hkAabb
import struct


class hkcdDynamicTreeCodecRawunsignedint(object):
    aabb: hkAabb
    parent: int
    children: int

    def __init__(self, infile):
        self.aabb = hkAabb(infile)  # TYPE_STRUCT
        self.parent = struct.unpack('>I', infile.read(4))
        self.children = struct.unpack('>I', infile.read(4))
