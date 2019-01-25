from .hkpShape import hkpShape
import struct
from .common import any
from .hkpCdBody import hkpCdBody


class hkpCdBody(object):
    shape: hkpShape
    shapeKey: int
    motion: any
    parent: hkpCdBody

    def __init__(self, infile):
        self.shape = hkpShape(infile)  # TYPE_POINTER
        self.shapeKey = struct.unpack('>I', infile.read(4))
        self.motion = any(infile)  # TYPE_POINTER
        self.parent = hkpCdBody(infile)  # TYPE_POINTER
