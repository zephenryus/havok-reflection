import struct


class hkaiNavMeshClearanceCacheManagerCacheInfo(object):
    clearanceCeiling: float

    def __init__(self, infile):
        self.clearanceCeiling = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID

    def __repr__(self):
        return "<{class_name} clearanceCeiling={clearanceCeiling}>".format(**{
            "class_name": self.__class__.__name__,
            "clearanceCeiling": self.clearanceCeiling,
        })
