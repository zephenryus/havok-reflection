from .hkContactPoint import hkContactPoint
import struct


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

    def __init__(self, infile):
        self.contactPoint = hkContactPoint(infile)  # TYPE_STRUCT:TYPE_VOID
        self.contactFriction = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.contactBody = any(infile)  # TYPE_POINTER:TYPE_VOID
        self.contactShapeKey = struct.unpack('>I', infile.read(4))  # TYPE_UINT32:TYPE_VOID
        self.hardPointWs = struct.unpack('>4f', infile.read(16))  # TYPE_VECTOR4:TYPE_VOID
        self.rayEndPointWs = struct.unpack('>4f', infile.read(16))  # TYPE_VECTOR4:TYPE_VOID
        self.currentSuspensionLength = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.suspensionDirectionWs = struct.unpack('>4f', infile.read(16))  # TYPE_VECTOR4:TYPE_VOID
        self.spinAxisChassisSpace = struct.unpack('>4f', infile.read(16))  # TYPE_VECTOR4:TYPE_VOID
        self.spinAxisWs = struct.unpack('>4f', infile.read(16))  # TYPE_VECTOR4:TYPE_VOID
        self.steeringOrientationChassisSpace = any(infile)  # TYPE_QUATERNION:TYPE_VOID
        self.spinVelocity = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.noSlipIdealSpinVelocity = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.spinAngle = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.skidEnergyDensity = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.sideForce = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.forwardSlipVelocity = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.sideSlipVelocity = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID

    def __repr__(self):
        return "<{class_name} contactPoint={contactPoint}, contactFriction={contactFriction}, contactBody={contactBody}, contactShapeKey={contactShapeKey}, hardPointWs={hardPointWs}, rayEndPointWs={rayEndPointWs}, currentSuspensionLength={currentSuspensionLength}, suspensionDirectionWs={suspensionDirectionWs}, spinAxisChassisSpace={spinAxisChassisSpace}, spinAxisWs={spinAxisWs}, steeringOrientationChassisSpace={steeringOrientationChassisSpace}, spinVelocity={spinVelocity}, noSlipIdealSpinVelocity={noSlipIdealSpinVelocity}, spinAngle={spinAngle}, skidEnergyDensity={skidEnergyDensity}, sideForce={sideForce}, forwardSlipVelocity={forwardSlipVelocity}, sideSlipVelocity={sideSlipVelocity}>".format(**{
            "class_name": self.__class__.__name__,
            "contactPoint": self.contactPoint,
            "contactFriction": self.contactFriction,
            "contactBody": self.contactBody,
            "contactShapeKey": self.contactShapeKey,
            "hardPointWs": self.hardPointWs,
            "rayEndPointWs": self.rayEndPointWs,
            "currentSuspensionLength": self.currentSuspensionLength,
            "suspensionDirectionWs": self.suspensionDirectionWs,
            "spinAxisChassisSpace": self.spinAxisChassisSpace,
            "spinAxisWs": self.spinAxisWs,
            "steeringOrientationChassisSpace": self.steeringOrientationChassisSpace,
            "spinVelocity": self.spinVelocity,
            "noSlipIdealSpinVelocity": self.noSlipIdealSpinVelocity,
            "spinAngle": self.spinAngle,
            "skidEnergyDensity": self.skidEnergyDensity,
            "sideForce": self.sideForce,
            "forwardSlipVelocity": self.forwardSlipVelocity,
            "sideSlipVelocity": self.sideSlipVelocity,
        })
