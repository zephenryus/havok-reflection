from .hkpConstraintAtom import hkpConstraintAtom
from .common import any, vector4


class hkpDeformableAngConstraintAtom(hkpConstraintAtom):
    offset: any
    yieldStrengthDiag: vector4
    yieldStrengthOffDiag: vector4
    ultimateStrengthDiag: vector4
    ultimateStrengthOffDiag: vector4
