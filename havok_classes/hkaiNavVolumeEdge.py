from .common import any
import struct


class hkaiNavVolumeEdge(object):
    flags: any
    oppositeCell: int

    def __init__(self, infile):
        self.flags = any(infile)  # TYPE_FLAGS
        self.oppositeCell = struct.unpack('>I', infile.read(4))
