from .hkaiNavVolumeMediator import hkaiNavVolumeMediator
from .hkaiNavVolume import hkaiNavVolume
from .hkcdStaticAabbTree import hkcdStaticAabbTree


class hkaiAabbTreeNavVolumeMediator(hkaiNavVolumeMediator):
    navVolume: hkaiNavVolume
    tree: hkcdStaticAabbTree

    def __init__(self, infile):
        self.navVolume = hkaiNavVolume(infile)  # TYPE_POINTER
        self.tree = hkcdStaticAabbTree(infile)  # TYPE_POINTER
