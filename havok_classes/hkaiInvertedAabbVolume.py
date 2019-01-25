from .hkaiVolume import hkaiVolume
from .hkAabb import hkAabb
from .hkGeometry import hkGeometry


class hkaiInvertedAabbVolume(hkaiVolume):
    aabb: hkAabb
    geometry: hkGeometry

    def __init__(self, infile):
        self.aabb = hkAabb(infile)  # TYPE_STRUCT:TYPE_VOID
        self.geometry = hkGeometry(infile)  # TYPE_STRUCT:TYPE_VOID

    def __repr__(self):
        return "<{class_name} aabb={aabb}, geometry={geometry}>".format(**{
            "class_name": self.__class__.__name__,
            "aabb": self.aabb,
            "geometry": self.geometry,
        })
