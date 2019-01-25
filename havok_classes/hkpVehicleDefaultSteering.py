from .hkpVehicleSteering import hkpVehicleSteering
import struct
from .common import any


class hkpVehicleDefaultSteering(hkpVehicleSteering):
    maxSteeringAngle: float
    maxSpeedFullSteeringAngle: float
    doesWheelSteer: any

    def __init__(self, infile):
        self.maxSteeringAngle = struct.unpack('>f', infile.read(4))
        self.maxSpeedFullSteeringAngle = struct.unpack('>f', infile.read(4))
        self.doesWheelSteer = any(infile)  # TYPE_ARRAY
