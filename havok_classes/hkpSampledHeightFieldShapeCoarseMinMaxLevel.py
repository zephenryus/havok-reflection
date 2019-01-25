from .common import any
import struct


class hkpSampledHeightFieldShapeCoarseMinMaxLevel(object):
    minMaxData: any
    xRes: int
    zRes: int

    def __init__(self, infile):
        self.minMaxData = any(infile)  # TYPE_ARRAY
        self.xRes = struct.unpack('>i', infile.read(4))
        self.zRes = struct.unpack('>i', infile.read(4))
