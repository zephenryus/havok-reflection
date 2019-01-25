from .hkReferencedObject import hkReferencedObject
from typing import List
from .common import get_array
from .hkpVehicleSuspensionSuspensionWheelParameters import hkpVehicleSuspensionSuspensionWheelParameters


class hkpVehicleSuspension(hkReferencedObject):
    wheelParams: List[hkpVehicleSuspensionSuspensionWheelParameters]

    def __init__(self, infile):
        self.wheelParams = get_array(infile, hkpVehicleSuspensionSuspensionWheelParameters, 0)  # TYPE_ARRAY:TYPE_STRUCT

    def __repr__(self):
        return "<{class_name} wheelParams=[{wheelParams}]>".format(**{
            "class_name": self.__class__.__name__,
            "wheelParams": self.wheelParams,
        })
