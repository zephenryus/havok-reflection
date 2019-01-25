import struct
from .hkaiAstarEdgeFilter import hkaiAstarEdgeFilter


class hkaiNavMeshClearanceCacheManagerRegistration(object):
    id: int
    info: int
    infoMask: int
    cacheIdentifier: int
    filter: any

    def __init__(self, infile):
        self.id = struct.unpack('>L', infile.read(8))  # TYPE_ULONG:TYPE_VOID
        self.info = struct.unpack('>I', infile.read(4))  # TYPE_UINT32:TYPE_VOID
        self.infoMask = struct.unpack('>I', infile.read(4))  # TYPE_UINT32:TYPE_VOID
        self.cacheIdentifier = struct.unpack('>B', infile.read(1))  # TYPE_UINT8:TYPE_VOID
        self.filter = any(infile)  # TYPE_POINTER:TYPE_STRUCT

    def __repr__(self):
        return "<{class_name} id={id}, info={info}, infoMask={infoMask}, cacheIdentifier={cacheIdentifier}, filter={filter}>".format(**{
            "class_name": self.__class__.__name__,
            "id": self.id,
            "info": self.info,
            "infoMask": self.infoMask,
            "cacheIdentifier": self.cacheIdentifier,
            "filter": self.filter,
        })
