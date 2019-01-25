import struct


class hkaiNavMeshClearanceCacheManagerCacheInfo(object):
    clearanceCeiling: float

    def __init__(self, infile):
        self.clearanceCeiling = struct.unpack('>f', infile.read(4))
