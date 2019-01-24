from .hkReferencedObject import hkReferencedObject
from .common import vector4, any
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
