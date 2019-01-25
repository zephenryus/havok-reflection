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
from .common import any
import struct


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

    def __init__(self, infile):
        self.data = hkpVehicleData(infile)  # TYPE_POINTER
        self.driverInput = hkpVehicleDriverInput(infile)  # TYPE_POINTER
        self.steering = hkpVehicleSteering(infile)  # TYPE_POINTER
        self.engine = hkpVehicleEngine(infile)  # TYPE_POINTER
        self.transmission = hkpVehicleTransmission(infile)  # TYPE_POINTER
        self.brake = hkpVehicleBrake(infile)  # TYPE_POINTER
        self.suspension = hkpVehicleSuspension(infile)  # TYPE_POINTER
        self.aerodynamics = hkpVehicleAerodynamics(infile)  # TYPE_POINTER
        self.wheelCollide = hkpVehicleWheelCollide(infile)  # TYPE_POINTER
        self.tyreMarks = hkpTyremarksInfo(infile)  # TYPE_POINTER
        self.velocityDamper = hkpVehicleVelocityDamper(infile)  # TYPE_POINTER
        self.vehicleSimulation = hkpVehicleSimulation(infile)  # TYPE_POINTER
        self.wheelsInfo = hkpVehicleInstanceWheelInfo(infile)  # TYPE_ARRAY
        self.deviceStatus = hkpVehicleDriverInputStatus(infile)  # TYPE_POINTER
        self.isFixed = any(infile)  # TYPE_ARRAY
        self.wheelsTimeSinceMaxPedalInput = struct.unpack('>f', infile.read(4))
        self.tryingToReverse = struct.unpack('>?', infile.read(1))
        self.torque = struct.unpack('>f', infile.read(4))
        self.rpm = struct.unpack('>f', infile.read(4))
        self.mainSteeringAngle = struct.unpack('>f', infile.read(4))
        self.mainSteeringAngleAssumingNoReduction = struct.unpack('>f', infile.read(4))
        self.wheelsSteeringAngle = any(infile)  # TYPE_ARRAY
        self.isReversing = struct.unpack('>?', infile.read(1))
        self.currentGear = struct.unpack('>b', infile.read(1))
        self.delayed = struct.unpack('>?', infile.read(1))
        self.clutchDelayCountdown = struct.unpack('>f', infile.read(4))
