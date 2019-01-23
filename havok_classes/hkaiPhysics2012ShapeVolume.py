from .hkaiVolume import hkaiVolume
from .hkpShape import hkpShape
from .hkGeometry import hkGeometry


class hkaiPhysics2012ShapeVolume(hkaiVolume):
	dispatcher: any
	shape: hkpShape
	shapeTransform: any
	geometry: hkGeometry
