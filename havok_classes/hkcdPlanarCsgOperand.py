from .hkReferencedObject import hkReferencedObject
from .hkcdPlanarSolid import hkcdPlanarSolid
from .hkcdPlanarGeometry import hkcdPlanarGeometry


class hkcdPlanarCsgOperand(hkReferencedObject):
    solid: any
    danglingGeometry: any
    regions: any

    def __init__(self, infile):
        self.solid = any(infile)  # TYPE_POINTER:TYPE_STRUCT
        self.danglingGeometry = any(infile)  # TYPE_POINTER:TYPE_STRUCT
        self.regions = any(infile)  # TYPE_POINTER:TYPE_VOID

    def __repr__(self):
        return "<{class_name} solid={solid}, danglingGeometry={danglingGeometry}, regions={regions}>".format(**{
            "class_name": self.__class__.__name__,
            "solid": self.solid,
            "danglingGeometry": self.danglingGeometry,
            "regions": self.regions,
        })
