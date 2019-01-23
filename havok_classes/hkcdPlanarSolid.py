from .hkcdPlanarEntity import hkcdPlanarEntity
from .hkcdPlanarSolidNodeStorage import hkcdPlanarSolidNodeStorage
from .hkcdPlanarGeometryPlanesCollection import hkcdPlanarGeometryPlanesCollection


class hkcdPlanarSolid(hkcdPlanarEntity):
	nodes: hkcdPlanarSolidNodeStorage
	planes: hkcdPlanarGeometryPlanesCollection
	rootNodeId: int
