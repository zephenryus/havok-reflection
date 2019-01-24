from .hkpModifierConstraintAtom import hkpModifierConstraintAtom
from .common import vector4


class hkpMassChangerModifierConstraintAtom(hkpModifierConstraintAtom):
    factorA: vector4
    factorB: vector4
