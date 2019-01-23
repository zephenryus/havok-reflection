from .hkpConstraintAtom import hkpConstraintAtom
from .hkUFloat8 import hkUFloat8


class hkpBallSocketConstraintAtom(hkpConstraintAtom):
	solvingMethod: any
	bodiesToNotify: int
	velocityStabilizationFactor: hkUFloat8
	enableLinearImpulseLimit: bool
	breachImpulse: float
	inertiaStabilizationFactor: float
