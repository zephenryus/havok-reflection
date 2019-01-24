from .hkaiNavVolumeMediator import hkaiNavVolumeMediator
from .hkaiStreamingCollection import hkaiStreamingCollection
from .hkcdDynamicAabbTree import hkcdDynamicAabbTree


class hkaiDynamicNavVolumeMediator(hkaiNavVolumeMediator):
    collection: hkaiStreamingCollection
    aabbTree: hkcdDynamicAabbTree
