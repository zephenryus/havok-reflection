from .hkpConstraintAtom import hkpConstraintAtom
from .common import any
from .hkpConstraintData import hkpConstraintData


class hkpBridgeConstraintAtom(hkpConstraintAtom):
    buildJacobianFunc: any
    constraintData: hkpConstraintData
    padding: int
