from .hkpVehicleSimulation import hkpVehicleSimulation
from .hkpVehicleFrictionStatus import hkpVehicleFrictionStatus
from .hkpVehicleFrictionDescription import hkpVehicleFrictionDescription


class hkpVehicleDefaultSimulation(hkpVehicleSimulation):
    frictionStatus: hkpVehicleFrictionStatus
    frictionDescription: hkpVehicleFrictionDescription

    def __init__(self, infile):
        self.frictionStatus = hkpVehicleFrictionStatus(infile)  # TYPE_STRUCT
        self.frictionDescription = hkpVehicleFrictionDescription(infile)  # TYPE_POINTER
