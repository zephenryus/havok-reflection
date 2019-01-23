from .hkReferencedObject import hkReferencedObject
from .hclShape import hclShape


class hclCollidable(hkReferencedObject):
	name: any
	transform: any
	linearVelocity: any
	angularVelocity: any
	pinchDetectionEnabled: bool
	pinchDetectionPriority: int
	pinchDetectionRadius: float
	shape: hclShape
