from .hkpVehicleWheelCollide import hkpVehicleWheelCollide
import struct
from .hkpAabbPhantom import hkpAabbPhantom
from .hkpRejectChassisListener import hkpRejectChassisListener


class hkpVehicleRayCastWheelCollide(hkpVehicleWheelCollide):
    wheelCollisionFilterInfo: int
    phantom: any
    rejectRayChassisListener: hkpRejectChassisListener

    def __init__(self, infile):
        self.wheelCollisionFilterInfo = struct.unpack('>I', infile.read(4))  # TYPE_UINT32:TYPE_VOID
        self.phantom = any(infile)  # TYPE_POINTER:TYPE_STRUCT
        self.rejectRayChassisListener = hkpRejectChassisListener(infile)  # TYPE_STRUCT:TYPE_VOID

    def __repr__(self):
        return "<{class_name} wheelCollisionFilterInfo={wheelCollisionFilterInfo}, phantom={phantom}, rejectRayChassisListener={rejectRayChassisListener}>".format(**{
            "class_name": self.__class__.__name__,
            "wheelCollisionFilterInfo": self.wheelCollisionFilterInfo,
            "phantom": self.phantom,
            "rejectRayChassisListener": self.rejectRayChassisListener,
        })
