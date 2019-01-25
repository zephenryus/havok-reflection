from .hkReferencedObject import hkReferencedObject
import struct
from .hkpVehicleFrictionDescriptionAxisDescription import hkpVehicleFrictionDescriptionAxisDescription


class hkpVehicleFrictionDescription(hkReferencedObject):
    wheelDistance: float
    chassisMassInv: float
    axleDescr: hkpVehicleFrictionDescriptionAxisDescription

    def __init__(self, infile):
        self.wheelDistance = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.chassisMassInv = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.axleDescr = hkpVehicleFrictionDescriptionAxisDescription(infile)  # TYPE_STRUCT:TYPE_VOID

    def __repr__(self):
        return "<{class_name} wheelDistance={wheelDistance}, chassisMassInv={chassisMassInv}, axleDescr={axleDescr}>".format(**{
            "class_name": self.__class__.__name__,
            "wheelDistance": self.wheelDistance,
            "chassisMassInv": self.chassisMassInv,
            "axleDescr": self.axleDescr,
        })
