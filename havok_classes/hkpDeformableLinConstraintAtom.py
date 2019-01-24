from .hkpConstraintAtom import hkpConstraintAtom
from .common import vector4


class hkpDeformableLinConstraintAtom(hkpConstraintAtom):
    offset: vector4
    yieldStrengthDiag: vector4
    yieldStrengthOffDiag: vector4
    ultimateStrengthDiag: vector4
    ultimateStrengthOffDiag: vector4
