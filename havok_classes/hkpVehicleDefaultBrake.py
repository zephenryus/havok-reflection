from .hkpVehicleBrake import hkpVehicleBrake
from .hkpVehicleDefaultBrakeWheelBrakingProperties import hkpVehicleDefaultBrakeWheelBrakingProperties
import struct


class hkpVehicleDefaultBrake(hkpVehicleBrake):
    wheelBrakingProperties: hkpVehicleDefaultBrakeWheelBrakingProperties
    wheelsMinTimeToBlock: float

    def __init__(self, infile):
        self.wheelBrakingProperties = hkpVehicleDefaultBrakeWheelBrakingProperties(infile)  # TYPE_ARRAY
        self.wheelsMinTimeToBlock = struct.unpack('>f', infile.read(4))
