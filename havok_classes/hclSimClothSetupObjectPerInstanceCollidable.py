from .hclCollidable import hclCollidable
from .hclVertexSelectionInput import hclVertexSelectionInput


class hclSimClothSetupObjectPerInstanceCollidable(object):
	collidable: hclCollidable
	collidingParticles: hclVertexSelectionInput
	drivingBoneName: any
	pinchDetectionEnabled: bool
	pinchDetectionPriority: int
	pinchDetectionRadius: float
