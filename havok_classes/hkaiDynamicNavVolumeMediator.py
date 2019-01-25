from .hkaiNavVolumeMediator import hkaiNavVolumeMediator
from .hkaiStreamingCollection import hkaiStreamingCollection
from .hkcdDynamicAabbTree import hkcdDynamicAabbTree


class hkaiDynamicNavVolumeMediator(hkaiNavVolumeMediator):
    collection: hkaiStreamingCollection
    aabbTree: hkcdDynamicAabbTree

    def __init__(self, infile):
        self.collection = hkaiStreamingCollection(infile)  # TYPE_POINTER
        self.aabbTree = hkcdDynamicAabbTree(infile)  # TYPE_POINTER
