from .hkpConstraintAtom import hkpConstraintAtom
from .hkpConstraintMotor import hkpConstraintMotor


class hkpAngMotorConstraintAtom(hkpConstraintAtom):
	isEnabled: bool
	motorAxis: int
	initializedOffset: int
	previousTargetAngleOffset: int
	motor: hkpConstraintMotor
	targetAngle: float
	correspondingAngLimitSolverResultOffset: int
	padding: int
