from .hkpConstraintAtom import hkpConstraintAtom


class hkpTwistLimitConstraintAtom(hkpConstraintAtom):
    isEnabled: int
    twistAxis: int
    refAxis: int
    minAngle: float
    maxAngle: float
    angularLimitsTauFactor: float
    angularLimitsDampFactor: float
    padding: int
