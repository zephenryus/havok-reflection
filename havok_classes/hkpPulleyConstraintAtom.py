from .hkpConstraintAtom import hkpConstraintAtom
from .common import vector4


class hkpPulleyConstraintAtom(hkpConstraintAtom):
    fixedPivotAinWorld: vector4
    fixedPivotBinWorld: vector4
    ropeLength: float
    leverageOnBodyB: float
