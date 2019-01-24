from .hkpWheelFrictionConstraintAtomAxle import hkpWheelFrictionConstraintAtomAxle
from .hkpWheelFrictionConstraintData import hkpWheelFrictionConstraintData
from .common import any, vector4


class hkpVehiclePerWheelSimulationWheelData(object):
    axle: hkpWheelFrictionConstraintAtomAxle
    frictionData: hkpWheelFrictionConstraintData
    frictionConstraint: any
    forwardDirectionWs: vector4
    sideDirectionWs: vector4
    contactLocal: vector4
