from .hkpVehicleWheelCollide import hkpVehicleWheelCollide
import struct
from .hkpAabbPhantom import hkpAabbPhantom
from .hkpRejectChassisListener import hkpRejectChassisListener


class hkpVehicleRayCastWheelCollide(hkpVehicleWheelCollide):
    wheelCollisionFilterInfo: int
    phantom: hkpAabbPhantom
    rejectRayChassisListener: hkpRejectChassisListener

    def __init__(self, infile):
        self.wheelCollisionFilterInfo = struct.unpack('>I', infile.read(4))
        self.phantom = hkpAabbPhantom(infile)  # TYPE_POINTER
        self.rejectRayChassisListener = hkpRejectChassisListener(infile)  # TYPE_STRUCT
