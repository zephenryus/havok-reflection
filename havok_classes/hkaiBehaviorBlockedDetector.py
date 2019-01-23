from .hkReferencedObject import hkReferencedObject
from .hkaiEdgeFollowingBehavior import hkaiEdgeFollowingBehavior


class hkaiBehaviorBlockedDetector(hkReferencedObject):
	behavior: hkaiEdgeFollowingBehavior
	prevRuntimeID: int
	prevPos: any
	avgProgress: float
	smoothingFactor: float
	blockedThreshold: float
	sqrTeleportationThreshold: float
	blocked: bool
