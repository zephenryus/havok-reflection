from .hkaiNavVolumeMediator import hkaiNavVolumeMediator
from .hkaiStreamingCollection import hkaiStreamingCollection
from .hkcdDynamicAabbTree import hkcdDynamicAabbTree


class hkaiDynamicNavVolumeMediator(hkaiNavVolumeMediator):
    collection: any
    aabbTree: any

    def __init__(self, infile):
        self.collection = any(infile)  # TYPE_POINTER:TYPE_STRUCT
        self.aabbTree = any(infile)  # TYPE_POINTER:TYPE_STRUCT

    def __repr__(self):
        return "<{class_name} collection={collection}, aabbTree={aabbTree}>".format(**{
            "class_name": self.__class__.__name__,
            "collection": self.collection,
            "aabbTree": self.aabbTree,
        })
