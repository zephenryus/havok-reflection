from .common import any
import struct


class hkpConstraintInstanceSmallArraySerializeOverrideType(object):
    data: any
    size: int
    capacityAndFlags: int

    def __init__(self, infile):
        self.data = any(infile)  # TYPE_POINTER
        self.size = struct.unpack('>H', infile.read(2))
        self.capacityAndFlags = struct.unpack('>H', infile.read(2))
