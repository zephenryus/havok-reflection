from .hkReferencedObject import hkReferencedObject
import struct
from .hkpVehicleFrictionDescriptionAxisDescription import hkpVehicleFrictionDescriptionAxisDescription


class hkpVehicleFrictionDescription(hkReferencedObject):
    wheelDistance: float
    chassisMassInv: float
    axleDescr: hkpVehicleFrictionDescriptionAxisDescription

    def __init__(self, infile):
        self.wheelDistance = struct.unpack('>f', infile.read(4))
        self.chassisMassInv = struct.unpack('>f', infile.read(4))
        self.axleDescr = hkpVehicleFrictionDescriptionAxisDescription(infile)  # TYPE_STRUCT
