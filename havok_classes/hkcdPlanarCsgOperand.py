from .hkReferencedObject import hkReferencedObject
from .hkcdPlanarSolid import hkcdPlanarSolid
from .hkcdPlanarGeometry import hkcdPlanarGeometry
from .common import any


class hkcdPlanarCsgOperand(hkReferencedObject):
    solid: hkcdPlanarSolid
    danglingGeometry: hkcdPlanarGeometry
    regions: any
