from .hkpVehicleEngine import hkpVehicleEngine
import struct


class hkpVehicleDefaultEngine(hkpVehicleEngine):
    minRPM: float
    optRPM: float
    maxRPM: float
    maxTorque: float
    torqueFactorAtMinRPM: float
    torqueFactorAtMaxRPM: float
    resistanceFactorAtMinRPM: float
    resistanceFactorAtOptRPM: float
    resistanceFactorAtMaxRPM: float
    clutchSlipRPM: float

    def __init__(self, infile):
        self.minRPM = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.optRPM = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.maxRPM = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.maxTorque = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.torqueFactorAtMinRPM = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.torqueFactorAtMaxRPM = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.resistanceFactorAtMinRPM = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.resistanceFactorAtOptRPM = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.resistanceFactorAtMaxRPM = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.clutchSlipRPM = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID

    def __repr__(self):
        return "<{class_name} minRPM={minRPM}, optRPM={optRPM}, maxRPM={maxRPM}, maxTorque={maxTorque}, torqueFactorAtMinRPM={torqueFactorAtMinRPM}, torqueFactorAtMaxRPM={torqueFactorAtMaxRPM}, resistanceFactorAtMinRPM={resistanceFactorAtMinRPM}, resistanceFactorAtOptRPM={resistanceFactorAtOptRPM}, resistanceFactorAtMaxRPM={resistanceFactorAtMaxRPM}, clutchSlipRPM={clutchSlipRPM}>".format(**{
            "class_name": self.__class__.__name__,
            "minRPM": self.minRPM,
            "optRPM": self.optRPM,
            "maxRPM": self.maxRPM,
            "maxTorque": self.maxTorque,
            "torqueFactorAtMinRPM": self.torqueFactorAtMinRPM,
            "torqueFactorAtMaxRPM": self.torqueFactorAtMaxRPM,
            "resistanceFactorAtMinRPM": self.resistanceFactorAtMinRPM,
            "resistanceFactorAtOptRPM": self.resistanceFactorAtOptRPM,
            "resistanceFactorAtMaxRPM": self.resistanceFactorAtMaxRPM,
            "clutchSlipRPM": self.clutchSlipRPM,
        })
