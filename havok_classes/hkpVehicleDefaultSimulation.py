from .hkpVehicleSimulation import hkpVehicleSimulation
from .hkpVehicleFrictionStatus import hkpVehicleFrictionStatus
from .hkpVehicleFrictionDescription import hkpVehicleFrictionDescription


class hkpVehicleDefaultSimulation(hkpVehicleSimulation):
    frictionStatus: hkpVehicleFrictionStatus
    frictionDescription: hkpVehicleFrictionDescription
