from .hkpCdBody import hkpCdBody
from enum import Enum
import struct
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

    def __init__(self, infile):
        self.ownerOffset = struct.unpack('>b', infile.read(1))  # TYPE_INT8:TYPE_VOID
        self.forceCollideOntoPpu = struct.unpack('>B', infile.read(1))  # TYPE_UINT8:TYPE_VOID
        self.shapeSizeOnSpu = struct.unpack('>H', infile.read(2))  # TYPE_UINT16:TYPE_VOID
        self.broadPhaseHandle = hkpTypedBroadPhaseHandle(infile)  # TYPE_STRUCT:TYPE_VOID
        self.boundingVolumeData = hkpCollidableBoundingVolumeData(infile)  # TYPE_STRUCT:TYPE_VOID
        self.allowedPenetrationDepth = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID

    def __repr__(self):
        return "<{class_name} ownerOffset={ownerOffset}, forceCollideOntoPpu={forceCollideOntoPpu}, shapeSizeOnSpu={shapeSizeOnSpu}, broadPhaseHandle={broadPhaseHandle}, boundingVolumeData={boundingVolumeData}, allowedPenetrationDepth={allowedPenetrationDepth}>".format(**{
            "class_name": self.__class__.__name__,
            "ownerOffset": self.ownerOffset,
            "forceCollideOntoPpu": self.forceCollideOntoPpu,
            "shapeSizeOnSpu": self.shapeSizeOnSpu,
            "broadPhaseHandle": self.broadPhaseHandle,
            "boundingVolumeData": self.boundingVolumeData,
            "allowedPenetrationDepth": self.allowedPenetrationDepth,
        })
