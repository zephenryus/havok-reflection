from .hkpVehicleTransmission import hkpVehicleTransmission
import struct
from typing import List
from .common import get_array


class hkpVehicleDefaultTransmission(hkpVehicleTransmission):
    downshiftRPM: float
    upshiftRPM: float
    primaryTransmissionRatio: float
    clutchDelayTime: float
    reverseGearRatio: float
    gearsRatio: List[float]
    wheelsTorqueRatio: List[float]

    def __init__(self, infile):
        self.downshiftRPM = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.upshiftRPM = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.primaryTransmissionRatio = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.clutchDelayTime = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.reverseGearRatio = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.gearsRatio = get_array(infile, float, 4)  # TYPE_ARRAY:TYPE_REAL
        self.wheelsTorqueRatio = get_array(infile, float, 4)  # TYPE_ARRAY:TYPE_REAL

    def __repr__(self):
        return "<{class_name} downshiftRPM={downshiftRPM}, upshiftRPM={upshiftRPM}, primaryTransmissionRatio={primaryTransmissionRatio}, clutchDelayTime={clutchDelayTime}, reverseGearRatio={reverseGearRatio}, gearsRatio=[{gearsRatio}], wheelsTorqueRatio=[{wheelsTorqueRatio}]>".format(**{
            "class_name": self.__class__.__name__,
            "downshiftRPM": self.downshiftRPM,
            "upshiftRPM": self.upshiftRPM,
            "primaryTransmissionRatio": self.primaryTransmissionRatio,
            "clutchDelayTime": self.clutchDelayTime,
            "reverseGearRatio": self.reverseGearRatio,
            "gearsRatio": self.gearsRatio,
            "wheelsTorqueRatio": self.wheelsTorqueRatio,
        })
