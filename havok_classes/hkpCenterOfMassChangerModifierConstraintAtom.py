from .hkpModifierConstraintAtom import hkpModifierConstraintAtom
from .common import vector4


class hkpCenterOfMassChangerModifierConstraintAtom(hkpModifierConstraintAtom):
    displacementA: vector4
    displacementB: vector4
