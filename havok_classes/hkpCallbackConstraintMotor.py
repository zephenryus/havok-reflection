from .hkpLimitedForceConstraintMotor import hkpLimitedForceConstraintMotor
from enum import Enum
from .enums import CallbackType
import struct


class CallbackType(Enum):
    CALLBACK_MOTOR_TYPE_HAVOK_DEMO_SPRING_DAMPER = 0
    CALLBACK_MOTOR_TYPE_USER_0 = 1
    CALLBACK_MOTOR_TYPE_USER_1 = 2
    CALLBACK_MOTOR_TYPE_USER_2 = 3
    CALLBACK_MOTOR_TYPE_USER_3 = 4


class hkpCallbackConstraintMotor(hkpLimitedForceConstraintMotor):
    callbackFunc: any
    callbackType: CallbackType
    userData0: int
    userData1: int
    userData2: int

    def __init__(self, infile):
        self.callbackFunc = any(infile)  # TYPE_POINTER:TYPE_VOID
        self.callbackType = CallbackType(infile)  # TYPE_ENUM:TYPE_UINT32
        self.userData0 = struct.unpack('>L', infile.read(8))  # TYPE_ULONG:TYPE_VOID
        self.userData1 = struct.unpack('>L', infile.read(8))  # TYPE_ULONG:TYPE_VOID
        self.userData2 = struct.unpack('>L', infile.read(8))  # TYPE_ULONG:TYPE_VOID

    def __repr__(self):
        return "<{class_name} callbackFunc={callbackFunc}, callbackType={callbackType}, userData0={userData0}, userData1={userData1}, userData2={userData2}>".format(**{
            "class_name": self.__class__.__name__,
            "callbackFunc": self.callbackFunc,
            "callbackType": self.callbackType,
            "userData0": self.userData0,
            "userData1": self.userData1,
            "userData2": self.userData2,
        })
