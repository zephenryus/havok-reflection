from .hkReferencedObject import hkReferencedObject
import struct
from typing import List
from .common import get_array
from .hkpTyremarksWheel import hkpTyremarksWheel


class hkpTyremarksInfo(hkReferencedObject):
    minTyremarkEnergy: float
    maxTyremarkEnergy: float
    tyremarksWheel: List[hkpTyremarksWheel]

    def __init__(self, infile):
        self.minTyremarkEnergy = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.maxTyremarkEnergy = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.tyremarksWheel = get_array(infile, hkpTyremarksWheel, 0)  # TYPE_ARRAY:TYPE_POINTER

    def __repr__(self):
        return "<{class_name} minTyremarkEnergy={minTyremarkEnergy}, maxTyremarkEnergy={maxTyremarkEnergy}, tyremarksWheel=[{tyremarksWheel}]>".format(**{
            "class_name": self.__class__.__name__,
            "minTyremarkEnergy": self.minTyremarkEnergy,
            "maxTyremarkEnergy": self.maxTyremarkEnergy,
            "tyremarksWheel": self.tyremarksWheel,
        })
