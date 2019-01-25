from .hkaiNavVolumeMediator import hkaiNavVolumeMediator
from .hkaiNavVolume import hkaiNavVolume
from .hkcdStaticAabbTree import hkcdStaticAabbTree


class hkaiAabbTreeNavVolumeMediator(hkaiNavVolumeMediator):
    navVolume: any
    tree: any

    def __init__(self, infile):
        self.navVolume = any(infile)  # TYPE_POINTER:TYPE_STRUCT
        self.tree = any(infile)  # TYPE_POINTER:TYPE_STRUCT

    def __repr__(self):
        return "<{class_name} navVolume={navVolume}, tree={tree}>".format(**{
            "class_name": self.__class__.__name__,
            "navVolume": self.navVolume,
            "tree": self.tree,
        })
