from .hkReferencedObject import hkReferencedObject
import struct
from .hkcdDynamicAabbTree import hkcdDynamicAabbTree
from .hkaiStreamingCollectionInstanceInfo import hkaiStreamingCollectionInstanceInfo
from .hkaiNavMeshClearanceCacheManager import hkaiNavMeshClearanceCacheManager


class hkaiStreamingCollection(hkReferencedObject):
    isTemporary: bool
    tree: hkcdDynamicAabbTree
    instances: hkaiStreamingCollectionInstanceInfo
    clearanceCacheManager: hkaiNavMeshClearanceCacheManager

    def __init__(self, infile):
        self.isTemporary = struct.unpack('>?', infile.read(1))
        self.tree = hkcdDynamicAabbTree(infile)  # TYPE_POINTER
        self.instances = hkaiStreamingCollectionInstanceInfo(infile)  # TYPE_ARRAY
        self.clearanceCacheManager = hkaiNavMeshClearanceCacheManager(infile)  # TYPE_POINTER
