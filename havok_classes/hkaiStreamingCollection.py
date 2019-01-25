from .hkReferencedObject import hkReferencedObject
import struct
from .hkcdDynamicAabbTree import hkcdDynamicAabbTree
from typing import List
from .common import get_array
from .hkaiStreamingCollectionInstanceInfo import hkaiStreamingCollectionInstanceInfo
from .hkaiNavMeshClearanceCacheManager import hkaiNavMeshClearanceCacheManager


class hkaiStreamingCollection(hkReferencedObject):
    isTemporary: bool
    tree: any
    instances: List[hkaiStreamingCollectionInstanceInfo]
    clearanceCacheManager: any

    def __init__(self, infile):
        self.isTemporary = struct.unpack('>?', infile.read(1))  # TYPE_BOOL:TYPE_VOID
        self.tree = any(infile)  # TYPE_POINTER:TYPE_STRUCT
        self.instances = get_array(infile, hkaiStreamingCollectionInstanceInfo, 0)  # TYPE_ARRAY:TYPE_STRUCT
        self.clearanceCacheManager = any(infile)  # TYPE_POINTER:TYPE_STRUCT

    def __repr__(self):
        return "<{class_name} isTemporary={isTemporary}, tree={tree}, instances=[{instances}], clearanceCacheManager={clearanceCacheManager}>".format(**{
            "class_name": self.__class__.__name__,
            "isTemporary": self.isTemporary,
            "tree": self.tree,
            "instances": self.instances,
            "clearanceCacheManager": self.clearanceCacheManager,
        })
