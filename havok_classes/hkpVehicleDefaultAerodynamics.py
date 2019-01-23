from .hkpVehicleAerodynamics import hkpVehicleAerodynamics


class hkpVehicleDefaultAerodynamics(hkpVehicleAerodynamics):
	airDensity: float
	frontalArea: float
	dragCoefficient: float
	liftCoefficient: float
	extraGravityws: any
