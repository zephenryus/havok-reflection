from .hkReferencedObject import hkReferencedObject
from .common import vector4, any
import struct
from .hkpVehicleDataWheelComponentParams import hkpVehicleDataWheelComponentParams


class hkpVehicleData(hkReferencedObject):
    gravity: vector4
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
    chassisFrictionInertiaInvDiag: vector4
    alreadyInitialised: bool

    def __init__(self, infile):
        self.gravity = struct.unpack('>4f', infile.read(16))
        self.numWheels = struct.unpack('>b', infile.read(1))
        self.chassisOrientation = any(infile)  # TYPE_ROTATION
        self.torqueRollFactor = struct.unpack('>f', infile.read(4))
        self.torquePitchFactor = struct.unpack('>f', infile.read(4))
        self.torqueYawFactor = struct.unpack('>f', infile.read(4))
        self.extraTorqueFactor = struct.unpack('>f', infile.read(4))
        self.maxVelocityForPositionalFriction = struct.unpack('>f', infile.read(4))
        self.chassisUnitInertiaYaw = struct.unpack('>f', infile.read(4))
        self.chassisUnitInertiaRoll = struct.unpack('>f', infile.read(4))
        self.chassisUnitInertiaPitch = struct.unpack('>f', infile.read(4))
        self.frictionEqualizer = struct.unpack('>f', infile.read(4))
        self.normalClippingAngleCos = struct.unpack('>f', infile.read(4))
        self.maxFrictionSolverMassRatio = struct.unpack('>f', infile.read(4))
        self.wheelParams = hkpVehicleDataWheelComponentParams(infile)  # TYPE_ARRAY
        self.numWheelsPerAxle = any(infile)  # TYPE_ARRAY
        self.chassisFrictionInertiaInvDiag = struct.unpack('>4f', infile.read(16))
        self.alreadyInitialised = struct.unpack('>?', infile.read(1))
