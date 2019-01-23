from .hkpConstraintAtom import hkpConstraintAtom


class hkpSetupStabilizationAtom(hkpConstraintAtom):
	enabled: bool
	padding: int
	maxLinImpulse: float
	maxAngImpulse: float
	maxAngle: float
