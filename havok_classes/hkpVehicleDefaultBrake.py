from .hkpVehicleBrake import hkpVehicleBrake
from typing import List
from .common import get_array
from .hkpVehicleDefaultBrakeWheelBrakingProperties import hkpVehicleDefaultBrakeWheelBrakingProperties
import struct


class hkpVehicleDefaultBrake(hkpVehicleBrake):
    wheelBrakingProperties: List[hkpVehicleDefaultBrakeWheelBrakingProperties]
    wheelsMinTimeToBlock: float

    def __init__(self, infile):
        self.wheelBrakingProperties = get_array(infile, hkpVehicleDefaultBrakeWheelBrakingProperties, 0)  # TYPE_ARRAY:TYPE_STRUCT
        self.wheelsMinTimeToBlock = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID

    def __repr__(self):
        return "<{class_name} wheelBrakingProperties=[{wheelBrakingProperties}], wheelsMinTimeToBlock={wheelsMinTimeToBlock}>".format(**{
            "class_name": self.__class__.__name__,
            "wheelBrakingProperties": self.wheelBrakingProperties,
            "wheelsMinTimeToBlock": self.wheelsMinTimeToBlock,
        })
