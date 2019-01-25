import struct
from .common import any


class hkaiNavMeshGenerationSettingsMaterialConstructionPair(object):
    materialIndex: int
    flags: any

    def __init__(self, infile):
        self.materialIndex = struct.unpack('>i', infile.read(4))
        self.flags = any(infile)  # TYPE_FLAGS
