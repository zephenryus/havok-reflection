from .hkReferencedObject import hkReferencedObject
from .hkpVehicleSuspensionSuspensionWheelParameters import hkpVehicleSuspensionSuspensionWheelParameters


class hkpVehicleSuspension(hkReferencedObject):
    wheelParams: hkpVehicleSuspensionSuspensionWheelParameters

    def __init__(self, infile):
        self.wheelParams = hkpVehicleSuspensionSuspensionWheelParameters(infile)  # TYPE_ARRAY
