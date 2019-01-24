from .hkpCdBody import hkpCdBody
from enum import Enum
from .hkpTypedBroadPhaseHandle import hkpTypedBroadPhaseHandle
from .hkpCollidableBoundingVolumeData import hkpCollidableBoundingVolumeData


class ForceCollideOntoPpuReasons(Enum):
    FORCE_PPU_USER_REQUEST = 1
    FORCE_PPU_SHAPE_REQUEST = 2
    FORCE_PPU_MODIFIER_REQUEST = 4
    FORCE_PPU_SHAPE_UNCHECKED = 8


class hkpCollidable(hkpCdBody):
    ownerOffset: int
    forceCollideOntoPpu: int
    shapeSizeOnSpu: int
    broadPhaseHandle: hkpTypedBroadPhaseHandle
    boundingVolumeData: hkpCollidableBoundingVolumeData
    allowedPenetrationDepth: float
