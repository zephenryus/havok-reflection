from .hkpBroadPhaseHandle import hkpBroadPhaseHandle


class hkpTypedBroadPhaseHandle(hkpBroadPhaseHandle):
	type: int
	ownerOffset: int
	objectQualityType: int
	collisionFilterInfo: int
