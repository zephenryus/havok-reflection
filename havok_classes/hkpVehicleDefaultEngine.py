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
        self.minRPM = struct.unpack('>f', infile.read(4))
        self.optRPM = struct.unpack('>f', infile.read(4))
        self.maxRPM = struct.unpack('>f', infile.read(4))
        self.maxTorque = struct.unpack('>f', infile.read(4))
        self.torqueFactorAtMinRPM = struct.unpack('>f', infile.read(4))
        self.torqueFactorAtMaxRPM = struct.unpack('>f', infile.read(4))
        self.resistanceFactorAtMinRPM = struct.unpack('>f', infile.read(4))
        self.resistanceFactorAtOptRPM = struct.unpack('>f', infile.read(4))
        self.resistanceFactorAtMaxRPM = struct.unpack('>f', infile.read(4))
        self.clutchSlipRPM = struct.unpack('>f', infile.read(4))
