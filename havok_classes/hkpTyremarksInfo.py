from .hkReferencedObject import hkReferencedObject
import struct
from .hkpTyremarksWheel import hkpTyremarksWheel


class hkpTyremarksInfo(hkReferencedObject):
    minTyremarkEnergy: float
    maxTyremarkEnergy: float
    tyremarksWheel: hkpTyremarksWheel

    def __init__(self, infile):
        self.minTyremarkEnergy = struct.unpack('>f', infile.read(4))
        self.maxTyremarkEnergy = struct.unpack('>f', infile.read(4))
        self.tyremarksWheel = hkpTyremarksWheel(infile)  # TYPE_ARRAY
