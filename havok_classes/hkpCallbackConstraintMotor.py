from .hkpLimitedForceConstraintMotor import hkpLimitedForceConstraintMotor
from enum import Enum
from .common import any
from .enums import CallbackType


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
