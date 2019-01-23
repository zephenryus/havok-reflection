from .hkpVehicleTransmission import hkpVehicleTransmission


class hkpVehicleDefaultTransmission(hkpVehicleTransmission):
	downshiftRPM: float
	upshiftRPM: float
	primaryTransmissionRatio: float
	clutchDelayTime: float
	reverseGearRatio: float
	gearsRatio: any
	wheelsTorqueRatio: any
