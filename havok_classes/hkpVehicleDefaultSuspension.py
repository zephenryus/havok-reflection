from .hkpVehicleSuspension import hkpVehicleSuspension
from .hkpVehicleDefaultSuspensionWheelSpringSuspensionParameters import hkpVehicleDefaultSuspensionWheelSpringSuspensionParameters


class hkpVehicleDefaultSuspension(hkpVehicleSuspension):
    wheelSpringParams: hkpVehicleDefaultSuspensionWheelSpringSuspensionParameters

    def __init__(self, infile):
        self.wheelSpringParams = hkpVehicleDefaultSuspensionWheelSpringSuspensionParameters(infile)  # TYPE_ARRAY
