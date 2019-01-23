from .hkpConstraintAtom import hkpConstraintAtom
from .hkpConstraintData import hkpConstraintData


class hkpBridgeConstraintAtom(hkpConstraintAtom):
	buildJacobianFunc: any
	constraintData: hkpConstraintData
	padding: int
