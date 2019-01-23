from .hkpUnaryAction import hkpUnaryAction


class hkpMouseSpringAction(hkpUnaryAction):
	positionInRbLocal: any
	mousePositionInWorld: any
	springDamping: float
	springElasticity: float
	maxRelativeForce: float
	objectDamping: float
	shapeKey: int
	applyCallbacks: any
