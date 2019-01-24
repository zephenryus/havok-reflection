from .hkpConstraintAtom import hkpConstraintAtom
from .enums import SolvingMethod
from .hkUFloat8 import hkUFloat8


class hkpBallSocketConstraintAtom(hkpConstraintAtom):
    solvingMethod: SolvingMethod
    bodiesToNotify: int
    velocityStabilizationFactor: hkUFloat8
    enableLinearImpulseLimit: bool
    breachImpulse: float
    inertiaStabilizationFactor: float
