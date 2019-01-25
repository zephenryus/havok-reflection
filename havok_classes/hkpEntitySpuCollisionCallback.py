from .common import any
import struct


class hkpEntitySpuCollisionCallback(object):
    util: any
    capacity: int
    eventFilter: int
    userFilter: int

    def __init__(self, infile):
        self.util = any(infile)  # TYPE_POINTER
        self.capacity = struct.unpack('>H', infile.read(2))
        self.eventFilter = struct.unpack('>B', infile.read(1))
        self.userFilter = struct.unpack('>B', infile.read(1))
