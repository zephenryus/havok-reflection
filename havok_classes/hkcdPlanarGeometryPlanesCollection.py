from .hkReferencedObject import hkReferencedObject
from .hkcdPlanarGeometryPrimitivesPlane import hkcdPlanarGeometryPrimitivesPlane


class hkcdPlanarGeometryPlanesCollection(hkReferencedObject):
	offsetAndScale: any
	planes: hkcdPlanarGeometryPrimitivesPlane
	cache: any
	criticalAccess: any
