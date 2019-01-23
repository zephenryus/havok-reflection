from .hkReferencedObject import hkReferencedObject
from .hkpVehicleDataWheelComponentParams import hkpVehicleDataWheelComponentParams


class hkpVehicleData(hkReferencedObject):
	gravity: any
	numWheels: int
	chassisOrientation: any
	torqueRollFactor: float
	torquePitchFactor: float
	torqueYawFactor: float
	extraTorqueFactor: float
	maxVelocityForPositionalFriction: float
	chassisUnitInertiaYaw: float
	chassisUnitInertiaRoll: float
	chassisUnitInertiaPitch: float
	frictionEqualizer: float
	normalClippingAngleCos: float
	maxFrictionSolverMassRatio: float
	wheelParams: hkpVehicleDataWheelComponentParams
	numWheelsPerAxle: any
	chassisFrictionInertiaInvDiag: any
	alreadyInitialised: bool
