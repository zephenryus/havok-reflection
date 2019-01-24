from .hkpConstraintAtom import hkpConstraintAtom


class hkpStiffSpringConstraintAtom(hkpConstraintAtom):
    length: float
    maxLength: float
    springConstant: float
    springDamping: float
