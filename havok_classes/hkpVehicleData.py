from .hkReferencedObject import hkReferencedObject
import struct
from typing import List
from .common import get_array
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
    wheelParams: List[hkpVehicleDataWheelComponentParams]
    numWheelsPerAxle: List[int]
    chassisFrictionInertiaInvDiag: vector4
    alreadyInitialised: bool

    def __init__(self, infile):
        self.gravity = struct.unpack('>4f', infile.read(16))  # TYPE_VECTOR4:TYPE_VOID
        self.numWheels = struct.unpack('>b', infile.read(1))  # TYPE_INT8:TYPE_VOID
        self.chassisOrientation = any(infile)  # TYPE_ROTATION:TYPE_VOID
        self.torqueRollFactor = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.torquePitchFactor = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.torqueYawFactor = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.extraTorqueFactor = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.maxVelocityForPositionalFriction = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.chassisUnitInertiaYaw = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.chassisUnitInertiaRoll = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.chassisUnitInertiaPitch = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.frictionEqualizer = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.normalClippingAngleCos = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.maxFrictionSolverMassRatio = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.wheelParams = get_array(infile, hkpVehicleDataWheelComponentParams, 0)  # TYPE_ARRAY:TYPE_STRUCT
        self.numWheelsPerAxle = get_array(infile, int, 1)  # TYPE_ARRAY:TYPE_INT8
        self.chassisFrictionInertiaInvDiag = struct.unpack('>4f', infile.read(16))  # TYPE_VECTOR4:TYPE_VOID
        self.alreadyInitialised = struct.unpack('>?', infile.read(1))  # TYPE_BOOL:TYPE_VOID

    def __repr__(self):
        return "<{class_name} gravity={gravity}, numWheels={numWheels}, chassisOrientation={chassisOrientation}, torqueRollFactor={torqueRollFactor}, torquePitchFactor={torquePitchFactor}, torqueYawFactor={torqueYawFactor}, extraTorqueFactor={extraTorqueFactor}, maxVelocityForPositionalFriction={maxVelocityForPositionalFriction}, chassisUnitInertiaYaw={chassisUnitInertiaYaw}, chassisUnitInertiaRoll={chassisUnitInertiaRoll}, chassisUnitInertiaPitch={chassisUnitInertiaPitch}, frictionEqualizer={frictionEqualizer}, normalClippingAngleCos={normalClippingAngleCos}, maxFrictionSolverMassRatio={maxFrictionSolverMassRatio}, wheelParams=[{wheelParams}], numWheelsPerAxle=[{numWheelsPerAxle}], chassisFrictionInertiaInvDiag={chassisFrictionInertiaInvDiag}, alreadyInitialised={alreadyInitialised}>".format(**{
            "class_name": self.__class__.__name__,
            "gravity": self.gravity,
            "numWheels": self.numWheels,
            "chassisOrientation": self.chassisOrientation,
            "torqueRollFactor": self.torqueRollFactor,
            "torquePitchFactor": self.torquePitchFactor,
            "torqueYawFactor": self.torqueYawFactor,
            "extraTorqueFactor": self.extraTorqueFactor,
            "maxVelocityForPositionalFriction": self.maxVelocityForPositionalFriction,
            "chassisUnitInertiaYaw": self.chassisUnitInertiaYaw,
            "chassisUnitInertiaRoll": self.chassisUnitInertiaRoll,
            "chassisUnitInertiaPitch": self.chassisUnitInertiaPitch,
            "frictionEqualizer": self.frictionEqualizer,
            "normalClippingAngleCos": self.normalClippingAngleCos,
            "maxFrictionSolverMassRatio": self.maxFrictionSolverMassRatio,
            "wheelParams": self.wheelParams,
            "numWheelsPerAxle": self.numWheelsPerAxle,
            "chassisFrictionInertiaInvDiag": self.chassisFrictionInertiaInvDiag,
            "alreadyInitialised": self.alreadyInitialised,
        })
