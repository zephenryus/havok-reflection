from .hkpVehicleSimulation import hkpVehicleSimulation
from .hkpVehicleFrictionStatus import hkpVehicleFrictionStatus
from .hkpVehicleFrictionDescription import hkpVehicleFrictionDescription


class hkpVehicleDefaultSimulation(hkpVehicleSimulation):
    frictionStatus: hkpVehicleFrictionStatus
    frictionDescription: any

    def __init__(self, infile):
        self.frictionStatus = hkpVehicleFrictionStatus(infile)  # TYPE_STRUCT:TYPE_VOID
        self.frictionDescription = any(infile)  # TYPE_POINTER:TYPE_STRUCT

    def __repr__(self):
        return "<{class_name} frictionStatus={frictionStatus}, frictionDescription={frictionDescription}>".format(**{
            "class_name": self.__class__.__name__,
            "frictionStatus": self.frictionStatus,
            "frictionDescription": self.frictionDescription,
        })
