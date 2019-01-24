from .hkpVehicleWheelCollide import hkpVehicleWheelCollide
from .hkpAabbPhantom import hkpAabbPhantom
from .hkpRejectChassisListener import hkpRejectChassisListener


class hkpVehicleRayCastWheelCollide(hkpVehicleWheelCollide):
    wheelCollisionFilterInfo: int
    phantom: hkpAabbPhantom
    rejectRayChassisListener: hkpRejectChassisListener
