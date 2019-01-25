from .enums import DataUsage
import struct


class hkxVertexAnimationUsageMap(object):
    use: DataUsage
    useIndexOrig: int
    useIndexLocal: int

    def __init__(self, infile):
        self.use = DataUsage(infile)  # TYPE_ENUM
        self.useIndexOrig = struct.unpack('>B', infile.read(1))
        self.useIndexLocal = struct.unpack('>B', infile.read(1))
