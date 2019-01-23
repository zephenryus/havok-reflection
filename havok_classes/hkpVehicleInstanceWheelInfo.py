from .hkContactPoint import hkContactPoint


class hkpVehicleInstanceWheelInfo(object):
	contactPoint: hkContactPoint
	contactFriction: float
	contactBody: any
	contactShapeKey: int
	hardPointWs: any
	rayEndPointWs: any
	currentSuspensionLength: float
	suspensionDirectionWs: any
	spinAxisChassisSpace: any
	spinAxisWs: any
	steeringOrientationChassisSpace: any
	spinVelocity: float
	noSlipIdealSpinVelocity: float
	spinAngle: float
	skidEnergyDensity: float
	sideForce: float
	forwardSlipVelocity: float
	sideSlipVelocity: float
