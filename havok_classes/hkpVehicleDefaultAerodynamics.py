from .hkpVehicleAerodynamics import hkpVehicleAerodynamics
import struct


class hkpVehicleDefaultAerodynamics(hkpVehicleAerodynamics):
    airDensity: float
    frontalArea: float
    dragCoefficient: float
    liftCoefficient: float
    extraGravityws: vector4

    def __init__(self, infile):
        self.airDensity = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.frontalArea = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.dragCoefficient = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.liftCoefficient = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.extraGravityws = struct.unpack('>4f', infile.read(16))  # TYPE_VECTOR4:TYPE_VOID

    def __repr__(self):
        return "<{class_name} airDensity={airDensity}, frontalArea={frontalArea}, dragCoefficient={dragCoefficient}, liftCoefficient={liftCoefficient}, extraGravityws={extraGravityws}>".format(**{
            "class_name": self.__class__.__name__,
            "airDensity": self.airDensity,
            "frontalArea": self.frontalArea,
            "dragCoefficient": self.dragCoefficient,
            "liftCoefficient": self.liftCoefficient,
            "extraGravityws": self.extraGravityws,
        })
