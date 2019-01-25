from .hkAabbHalf import hkAabbHalf
import struct


class hkcdDynamicTreeCodec18(object):
    aabb: hkAabbHalf
    parent: int

    def __init__(self, infile):
        self.aabb = hkAabbHalf(infile)  # TYPE_STRUCT
        self.parent = struct.unpack('>H', infile.read(2))
