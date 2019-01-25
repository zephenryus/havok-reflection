from .hkAabb import hkAabb
import struct


class hkcdDynamicTreeCodecRawunsignedlong(object):
    aabb: hkAabb
    parent: int
    children: int

    def __init__(self, infile):
        self.aabb = hkAabb(infile)  # TYPE_STRUCT
        self.parent = struct.unpack('>L', infile.read(8))
        self.children = struct.unpack('>L', infile.read(8))
