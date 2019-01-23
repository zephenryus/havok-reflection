from .hkpCdBody import hkpCdBody
from .hkpTypedBroadPhaseHandle import hkpTypedBroadPhaseHandle
from .hkpCollidableBoundingVolumeData import hkpCollidableBoundingVolumeData


class hkpCollidable(hkpCdBody):
	ownerOffset: int
	forceCollideOntoPpu: int
	shapeSizeOnSpu: int
	broadPhaseHandle: hkpTypedBroadPhaseHandle
	boundingVolumeData: hkpCollidableBoundingVolumeData
	allowedPenetrationDepth: float
