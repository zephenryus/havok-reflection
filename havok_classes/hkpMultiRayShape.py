from .hkpShape import hkpShape
from .hkpMultiRayShapeRay import hkpMultiRayShapeRay


class hkpMultiRayShape(hkpShape):
	rays: hkpMultiRayShapeRay
	rayPenetrationDistance: float
