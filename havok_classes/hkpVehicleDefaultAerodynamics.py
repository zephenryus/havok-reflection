from .hkpVehicleAerodynamics import hkpVehicleAerodynamics
from .common import vector4


class hkpVehicleDefaultAerodynamics(hkpVehicleAerodynamics):
    airDensity: float
    frontalArea: float
    dragCoefficient: float
    liftCoefficient: float
    extraGravityws: vector4
