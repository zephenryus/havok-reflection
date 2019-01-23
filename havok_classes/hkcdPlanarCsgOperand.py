from .hkReferencedObject import hkReferencedObject
from .hkcdPlanarSolid import hkcdPlanarSolid
from .hkcdPlanarGeometry import hkcdPlanarGeometry


class hkcdPlanarCsgOperand(hkReferencedObject):
	solid: hkcdPlanarSolid
	danglingGeometry: hkcdPlanarGeometry
	regions: any
