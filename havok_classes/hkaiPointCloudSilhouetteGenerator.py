from .hkaiSilhouetteGenerator import hkaiSilhouetteGenerator
from enum import Enum
from .hkAabb import hkAabb
from typing import List
from .common import get_array
import struct
from .enums import DetailLevel


class DetailLevel(Enum):
    DETAIL_INVALID = 0
    DETAIL_FULL = 1
    DETAIL_OBB = 2
    DETAIL_CONVEX_HULL = 3


class PointCloudFlagBits(Enum):
    LOCAL_POINTS_CHANGED = 1


class hkaiPointCloudSilhouetteGenerator(hkaiSilhouetteGenerator):
    localAabb: hkAabb
    localPoints: List[vector4]
    silhouetteSizes: List[int]
    weldTolerance: float
    silhouetteDetailLevel: DetailLevel
    flags: any
    localPointsChanged: bool
    isEnabled: bool

    def __init__(self, infile):
        self.localAabb = hkAabb(infile)  # TYPE_STRUCT:TYPE_VOID
        self.localPoints = get_array(infile, vector4, 16)  # TYPE_ARRAY:TYPE_VECTOR4
        self.silhouetteSizes = get_array(infile, int, 4)  # TYPE_ARRAY:TYPE_INT32
        self.weldTolerance = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.silhouetteDetailLevel = DetailLevel(infile)  # TYPE_ENUM:TYPE_UINT8
        self.flags = any(infile)  # TYPE_FLAGS:TYPE_UINT8
        self.localPointsChanged = struct.unpack('>?', infile.read(1))  # TYPE_BOOL:TYPE_VOID
        self.isEnabled = struct.unpack('>?', infile.read(1))  # TYPE_BOOL:TYPE_VOID

    def __repr__(self):
        return "<{class_name} localAabb={localAabb}, localPoints=[{localPoints}], silhouetteSizes=[{silhouetteSizes}], weldTolerance={weldTolerance}, silhouetteDetailLevel={silhouetteDetailLevel}, flags={flags}, localPointsChanged={localPointsChanged}, isEnabled={isEnabled}>".format(**{
            "class_name": self.__class__.__name__,
            "localAabb": self.localAabb,
            "localPoints": self.localPoints,
            "silhouetteSizes": self.silhouetteSizes,
            "weldTolerance": self.weldTolerance,
            "silhouetteDetailLevel": self.silhouetteDetailLevel,
            "flags": self.flags,
            "localPointsChanged": self.localPointsChanged,
            "isEnabled": self.isEnabled,
        })
