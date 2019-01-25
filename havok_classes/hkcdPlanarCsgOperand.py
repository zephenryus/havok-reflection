from .hkReferencedObject import hkReferencedObject
from .hkcdPlanarSolid import hkcdPlanarSolid
from .hkcdPlanarGeometry import hkcdPlanarGeometry
from .common import any


class hkcdPlanarCsgOperand(hkReferencedObject):
    solid: hkcdPlanarSolid
    danglingGeometry: hkcdPlanarGeometry
    regions: any

    def __init__(self, infile):
        self.solid = hkcdPlanarSolid(infile)  # TYPE_POINTER
        self.danglingGeometry = hkcdPlanarGeometry(infile)  # TYPE_POINTER
        self.regions = any(infile)  # TYPE_POINTER
