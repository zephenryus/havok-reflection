from .hkContactPoint import hkContactPoint
from .common import any, vector4


class hkpVehicleInstanceWheelInfo(object):
    contactPoint: hkContactPoint
    contactFriction: float
    contactBody: any
    contactShapeKey: int
    hardPointWs: vector4
    rayEndPointWs: vector4
    currentSuspensionLength: float
    suspensionDirectionWs: vector4
    spinAxisChassisSpace: vector4
    spinAxisWs: vector4
    steeringOrientationChassisSpace: any
    spinVelocity: float
    noSlipIdealSpinVelocity: float
    spinAngle: float
    skidEnergyDensity: float
    sideForce: float
    forwardSlipVelocity: float
    sideSlipVelocity: float
