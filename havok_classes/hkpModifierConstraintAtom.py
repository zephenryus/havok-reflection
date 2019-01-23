from .hkpConstraintAtom import hkpConstraintAtom
from .hkpConstraintAtom import hkpConstraintAtom


class hkpModifierConstraintAtom(hkpConstraintAtom):
	modifierAtomSize: int
	childSize: int
	child: hkpConstraintAtom
	pad: int
