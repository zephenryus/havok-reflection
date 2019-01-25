from .hkContactPoint import hkContactPoint
import struct
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

    def __init__(self, infile):
        self.contactPoint = hkContactPoint(infile)  # TYPE_STRUCT
        self.contactFriction = struct.unpack('>f', infile.read(4))
        self.contactBody = any(infile)  # TYPE_POINTER
        self.contactShapeKey = struct.unpack('>I', infile.read(4))
        self.hardPointWs = struct.unpack('>4f', infile.read(16))
        self.rayEndPointWs = struct.unpack('>4f', infile.read(16))
        self.currentSuspensionLength = struct.unpack('>f', infile.read(4))
        self.suspensionDirectionWs = struct.unpack('>4f', infile.read(16))
        self.spinAxisChassisSpace = struct.unpack('>4f', infile.read(16))
        self.spinAxisWs = struct.unpack('>4f', infile.read(16))
        self.steeringOrientationChassisSpace = any(infile)  # TYPE_QUATERNION
        self.spinVelocity = struct.unpack('>f', infile.read(4))
        self.noSlipIdealSpinVelocity = struct.unpack('>f', infile.read(4))
        self.spinAngle = struct.unpack('>f', infile.read(4))
        self.skidEnergyDensity = struct.unpack('>f', infile.read(4))
        self.sideForce = struct.unpack('>f', infile.read(4))
        self.forwardSlipVelocity = struct.unpack('>f', infile.read(4))
        self.sideSlipVelocity = struct.unpack('>f', infile.read(4))
