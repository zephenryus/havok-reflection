from .hkpConstraintAtom import hkpConstraintAtom


class hkpLinFrictionConstraintAtom(hkpConstraintAtom):
    isEnabled: int
    frictionAxis: int
    maxFrictionForce: float
    padding: int
