from .hkpVehicleSuspension import hkpVehicleSuspension
from typing import List
from .common import get_array
from .hkpVehicleDefaultSuspensionWheelSpringSuspensionParameters import hkpVehicleDefaultSuspensionWheelSpringSuspensionParameters


class hkpVehicleDefaultSuspension(hkpVehicleSuspension):
    wheelSpringParams: List[hkpVehicleDefaultSuspensionWheelSpringSuspensionParameters]

    def __init__(self, infile):
        self.wheelSpringParams = get_array(infile, hkpVehicleDefaultSuspensionWheelSpringSuspensionParameters, 0)  # TYPE_ARRAY:TYPE_STRUCT

    def __repr__(self):
        return "<{class_name} wheelSpringParams=[{wheelSpringParams}]>".format(**{
            "class_name": self.__class__.__name__,
            "wheelSpringParams": self.wheelSpringParams,
        })
