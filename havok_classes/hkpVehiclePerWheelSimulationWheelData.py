from .hkpWheelFrictionConstraintAtomAxle import hkpWheelFrictionConstraintAtomAxle
from .hkpWheelFrictionConstraintData import hkpWheelFrictionConstraintData


class hkpVehiclePerWheelSimulationWheelData(object):
	axle: hkpWheelFrictionConstraintAtomAxle
	frictionData: hkpWheelFrictionConstraintData
	frictionConstraint: any
	forwardDirectionWs: any
	sideDirectionWs: any
	contactLocal: any
