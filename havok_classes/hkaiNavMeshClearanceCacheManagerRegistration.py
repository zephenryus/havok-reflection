import struct
from .hkaiAstarEdgeFilter import hkaiAstarEdgeFilter


class hkaiNavMeshClearanceCacheManagerRegistration(object):
    id: int
    info: int
    infoMask: int
    cacheIdentifier: int
    filter: hkaiAstarEdgeFilter

    def __init__(self, infile):
        self.id = struct.unpack('>L', infile.read(8))
        self.info = struct.unpack('>I', infile.read(4))
        self.infoMask = struct.unpack('>I', infile.read(4))
        self.cacheIdentifier = struct.unpack('>B', infile.read(1))
        self.filter = hkaiAstarEdgeFilter(infile)  # TYPE_POINTER
