from .hkpUnaryAction import hkpUnaryAction
from .hkpVehicleData import hkpVehicleData
from .hkpVehicleDriverInput import hkpVehicleDriverInput
from .hkpVehicleSteering import hkpVehicleSteering
from .hkpVehicleEngine import hkpVehicleEngine
from .hkpVehicleTransmission import hkpVehicleTransmission
from .hkpVehicleBrake import hkpVehicleBrake
from .hkpVehicleSuspension import hkpVehicleSuspension
from .hkpVehicleAerodynamics import hkpVehicleAerodynamics
from .hkpVehicleWheelCollide import hkpVehicleWheelCollide
from .hkpTyremarksInfo import hkpTyremarksInfo
from .hkpVehicleVelocityDamper import hkpVehicleVelocityDamper
from .hkpVehicleSimulation import hkpVehicleSimulation
from .hkpVehicleInstanceWheelInfo import hkpVehicleInstanceWheelInfo
from .hkpVehicleDriverInputStatus import hkpVehicleDriverInputStatus


class hkpVehicleInstance(hkpUnaryAction):
	data: hkpVehicleData
	driverInput: hkpVehicleDriverInput
	steering: hkpVehicleSteering
	engine: hkpVehicleEngine
	transmission: hkpVehicleTransmission
	brake: hkpVehicleBrake
	suspension: hkpVehicleSuspension
	aerodynamics: hkpVehicleAerodynamics
	wheelCollide: hkpVehicleWheelCollide
	tyreMarks: hkpTyremarksInfo
	velocityDamper: hkpVehicleVelocityDamper
	vehicleSimulation: hkpVehicleSimulation
	wheelsInfo: hkpVehicleInstanceWheelInfo
	deviceStatus: hkpVehicleDriverInputStatus
	isFixed: any
	wheelsTimeSinceMaxPedalInput: float
	tryingToReverse: bool
	torque: float
	rpm: float
	mainSteeringAngle: float
	mainSteeringAngleAssumingNoReduction: float
	wheelsSteeringAngle: any
	isReversing: bool
	currentGear: int
	delayed: bool
	clutchDelayCountdown: float
