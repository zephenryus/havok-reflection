from .hkpVehicleWheelCollide import hkpVehicleWheelCollide
import struct
from .hkpVehicleLinearCastWheelCollideWheelState import hkpVehicleLinearCastWheelCollideWheelState
from .hkpRejectChassisListener import hkpRejectChassisListener


class hkpVehicleLinearCastWheelCollide(hkpVehicleWheelCollide):
    wheelCollisionFilterInfo: int
    wheelStates: hkpVehicleLinearCastWheelCollideWheelState
    rejectChassisListener: hkpRejectChassisListener
    maxExtraPenetration: float
    startPointTolerance: float
    collectStartPointHits: bool

    def __init__(self, infile):
        self.wheelCollisionFilterInfo = struct.unpack('>I', infile.read(4))
        self.wheelStates = hkpVehicleLinearCastWheelCollideWheelState(infile)  # TYPE_ARRAY
        self.rejectChassisListener = hkpRejectChassisListener(infile)  # TYPE_STRUCT
        self.maxExtraPenetration = struct.unpack('>f', infile.read(4))
        self.startPointTolerance = struct.unpack('>f', infile.read(4))
        self.collectStartPointHits = struct.unpack('>?', infile.read(1))
