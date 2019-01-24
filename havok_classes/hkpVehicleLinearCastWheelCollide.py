from .hkpVehicleWheelCollide import hkpVehicleWheelCollide
from .hkpVehicleLinearCastWheelCollideWheelState import hkpVehicleLinearCastWheelCollideWheelState
from .hkpRejectChassisListener import hkpRejectChassisListener


class hkpVehicleLinearCastWheelCollide(hkpVehicleWheelCollide):
    wheelCollisionFilterInfo: int
    wheelStates: hkpVehicleLinearCastWheelCollideWheelState
    rejectChassisListener: hkpRejectChassisListener
    maxExtraPenetration: float
    startPointTolerance: float
    collectStartPointHits: bool
