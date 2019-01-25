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
from typing import List
from .common import get_array
from .hkpVehicleInstanceWheelInfo import hkpVehicleInstanceWheelInfo
from .hkpVehicleDriverInputStatus import hkpVehicleDriverInputStatus
import struct


class hkpVehicleInstance(hkpUnaryAction):
    data: any
    driverInput: any
    steering: any
    engine: any
    transmission: any
    brake: any
    suspension: any
    aerodynamics: any
    wheelCollide: any
    tyreMarks: any
    velocityDamper: any
    vehicleSimulation: any
    wheelsInfo: List[hkpVehicleInstanceWheelInfo]
    deviceStatus: any
    isFixed: List[bool]
    wheelsTimeSinceMaxPedalInput: float
    tryingToReverse: bool
    torque: float
    rpm: float
    mainSteeringAngle: float
    mainSteeringAngleAssumingNoReduction: float
    wheelsSteeringAngle: List[float]
    isReversing: bool
    currentGear: int
    delayed: bool
    clutchDelayCountdown: float

    def __init__(self, infile):
        self.data = any(infile)  # TYPE_POINTER:TYPE_STRUCT
        self.driverInput = any(infile)  # TYPE_POINTER:TYPE_STRUCT
        self.steering = any(infile)  # TYPE_POINTER:TYPE_STRUCT
        self.engine = any(infile)  # TYPE_POINTER:TYPE_STRUCT
        self.transmission = any(infile)  # TYPE_POINTER:TYPE_STRUCT
        self.brake = any(infile)  # TYPE_POINTER:TYPE_STRUCT
        self.suspension = any(infile)  # TYPE_POINTER:TYPE_STRUCT
        self.aerodynamics = any(infile)  # TYPE_POINTER:TYPE_STRUCT
        self.wheelCollide = any(infile)  # TYPE_POINTER:TYPE_STRUCT
        self.tyreMarks = any(infile)  # TYPE_POINTER:TYPE_STRUCT
        self.velocityDamper = any(infile)  # TYPE_POINTER:TYPE_STRUCT
        self.vehicleSimulation = any(infile)  # TYPE_POINTER:TYPE_STRUCT
        self.wheelsInfo = get_array(infile, hkpVehicleInstanceWheelInfo, 0)  # TYPE_ARRAY:TYPE_STRUCT
        self.deviceStatus = any(infile)  # TYPE_POINTER:TYPE_STRUCT
        self.isFixed = get_array(infile, bool, 1)  # TYPE_ARRAY:TYPE_BOOL
        self.wheelsTimeSinceMaxPedalInput = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.tryingToReverse = struct.unpack('>?', infile.read(1))  # TYPE_BOOL:TYPE_VOID
        self.torque = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.rpm = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.mainSteeringAngle = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.mainSteeringAngleAssumingNoReduction = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.wheelsSteeringAngle = get_array(infile, float, 4)  # TYPE_ARRAY:TYPE_REAL
        self.isReversing = struct.unpack('>?', infile.read(1))  # TYPE_BOOL:TYPE_VOID
        self.currentGear = struct.unpack('>b', infile.read(1))  # TYPE_INT8:TYPE_VOID
        self.delayed = struct.unpack('>?', infile.read(1))  # TYPE_BOOL:TYPE_VOID
        self.clutchDelayCountdown = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID

    def __repr__(self):
        return "<{class_name} data={data}, driverInput={driverInput}, steering={steering}, engine={engine}, transmission={transmission}, brake={brake}, suspension={suspension}, aerodynamics={aerodynamics}, wheelCollide={wheelCollide}, tyreMarks={tyreMarks}, velocityDamper={velocityDamper}, vehicleSimulation={vehicleSimulation}, wheelsInfo=[{wheelsInfo}], deviceStatus={deviceStatus}, isFixed=[{isFixed}], wheelsTimeSinceMaxPedalInput={wheelsTimeSinceMaxPedalInput}, tryingToReverse={tryingToReverse}, torque={torque}, rpm={rpm}, mainSteeringAngle={mainSteeringAngle}, mainSteeringAngleAssumingNoReduction={mainSteeringAngleAssumingNoReduction}, wheelsSteeringAngle=[{wheelsSteeringAngle}], isReversing={isReversing}, currentGear={currentGear}, delayed={delayed}, clutchDelayCountdown={clutchDelayCountdown}>".format(**{
            "class_name": self.__class__.__name__,
            "data": self.data,
            "driverInput": self.driverInput,
            "steering": self.steering,
            "engine": self.engine,
            "transmission": self.transmission,
            "brake": self.brake,
            "suspension": self.suspension,
            "aerodynamics": self.aerodynamics,
            "wheelCollide": self.wheelCollide,
            "tyreMarks": self.tyreMarks,
            "velocityDamper": self.velocityDamper,
            "vehicleSimulation": self.vehicleSimulation,
            "wheelsInfo": self.wheelsInfo,
            "deviceStatus": self.deviceStatus,
            "isFixed": self.isFixed,
            "wheelsTimeSinceMaxPedalInput": self.wheelsTimeSinceMaxPedalInput,
            "tryingToReverse": self.tryingToReverse,
            "torque": self.torque,
            "rpm": self.rpm,
            "mainSteeringAngle": self.mainSteeringAngle,
            "mainSteeringAngleAssumingNoReduction": self.mainSteeringAngleAssumingNoReduction,
            "wheelsSteeringAngle": self.wheelsSteeringAngle,
            "isReversing": self.isReversing,
            "currentGear": self.currentGear,
            "delayed": self.delayed,
            "clutchDelayCountdown": self.clutchDelayCountdown,
        })
