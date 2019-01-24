from .hkpConstraintAtom import hkpConstraintAtom
from .hkpConstraintMotor import hkpConstraintMotor


class hkpLinMotorConstraintAtom(hkpConstraintAtom):
    isEnabled: bool
    motorAxis: int
    initializedOffset: int
    previousTargetPositionOffset: int
    motor: hkpConstraintMotor
    targetPosition: float
    padding: int
