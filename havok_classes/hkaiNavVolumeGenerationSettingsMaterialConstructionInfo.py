import struct
from .common import any


class hkaiNavVolumeGenerationSettingsMaterialConstructionInfo(object):
    materialIndex: int
    flags: any
    resolution: int

    def __init__(self, infile):
        self.materialIndex = struct.unpack('>i', infile.read(4))
        self.flags = any(infile)  # TYPE_FLAGS
        self.resolution = struct.unpack('>i', infile.read(4))
