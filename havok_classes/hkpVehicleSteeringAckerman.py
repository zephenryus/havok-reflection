from .hkpVehicleSteering import hkpVehicleSteering
import struct
from typing import List
from .common import get_array


class hkpVehicleSteeringAckerman(hkpVehicleSteering):
    maxSteeringAngle: float
    maxSpeedFullSteeringAngle: float
    doesWheelSteer: List[bool]
    trackWidth: float
    wheelBaseLength: float

    def __init__(self, infile):
        self.maxSteeringAngle = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.maxSpeedFullSteeringAngle = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.doesWheelSteer = get_array(infile, bool, 1)  # TYPE_ARRAY:TYPE_BOOL
        self.trackWidth = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.wheelBaseLength = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID

    def __repr__(self):
        return "<{class_name} maxSteeringAngle={maxSteeringAngle}, maxSpeedFullSteeringAngle={maxSpeedFullSteeringAngle}, doesWheelSteer=[{doesWheelSteer}], trackWidth={trackWidth}, wheelBaseLength={wheelBaseLength}>".format(**{
            "class_name": self.__class__.__name__,
            "maxSteeringAngle": self.maxSteeringAngle,
            "maxSpeedFullSteeringAngle": self.maxSpeedFullSteeringAngle,
            "doesWheelSteer": self.doesWheelSteer,
            "trackWidth": self.trackWidth,
            "wheelBaseLength": self.wheelBaseLength,
        })
