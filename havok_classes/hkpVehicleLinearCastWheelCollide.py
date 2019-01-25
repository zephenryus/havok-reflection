from .hkpVehicleWheelCollide import hkpVehicleWheelCollide
import struct
from typing import List
from .common import get_array
from .hkpVehicleLinearCastWheelCollideWheelState import hkpVehicleLinearCastWheelCollideWheelState
from .hkpRejectChassisListener import hkpRejectChassisListener


class hkpVehicleLinearCastWheelCollide(hkpVehicleWheelCollide):
    wheelCollisionFilterInfo: int
    wheelStates: List[hkpVehicleLinearCastWheelCollideWheelState]
    rejectChassisListener: hkpRejectChassisListener
    maxExtraPenetration: float
    startPointTolerance: float
    collectStartPointHits: bool

    def __init__(self, infile):
        self.wheelCollisionFilterInfo = struct.unpack('>I', infile.read(4))  # TYPE_UINT32:TYPE_VOID
        self.wheelStates = get_array(infile, hkpVehicleLinearCastWheelCollideWheelState, 0)  # TYPE_ARRAY:TYPE_STRUCT
        self.rejectChassisListener = hkpRejectChassisListener(infile)  # TYPE_STRUCT:TYPE_VOID
        self.maxExtraPenetration = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.startPointTolerance = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.collectStartPointHits = struct.unpack('>?', infile.read(1))  # TYPE_BOOL:TYPE_VOID

    def __repr__(self):
        return "<{class_name} wheelCollisionFilterInfo={wheelCollisionFilterInfo}, wheelStates=[{wheelStates}], rejectChassisListener={rejectChassisListener}, maxExtraPenetration={maxExtraPenetration}, startPointTolerance={startPointTolerance}, collectStartPointHits={collectStartPointHits}>".format(**{
            "class_name": self.__class__.__name__,
            "wheelCollisionFilterInfo": self.wheelCollisionFilterInfo,
            "wheelStates": self.wheelStates,
            "rejectChassisListener": self.rejectChassisListener,
            "maxExtraPenetration": self.maxExtraPenetration,
            "startPointTolerance": self.startPointTolerance,
            "collectStartPointHits": self.collectStartPointHits,
        })
