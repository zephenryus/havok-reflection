from .hkpConstraintAtom import hkpConstraintAtom
from .hkpConstraintMotor import hkpConstraintMotor


class hkpRagdollMotorConstraintAtom(hkpConstraintAtom):
	isEnabled: bool
	initializedOffset: int
	previousTargetAnglesOffset: int
	target_bRca: any
	motors: hkpConstraintMotor
