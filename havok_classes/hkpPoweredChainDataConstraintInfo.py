from .common import vector4, any
from .hkpConstraintMotor import hkpConstraintMotor


class hkpPoweredChainDataConstraintInfo(object):
    pivotInA: vector4
    pivotInB: vector4
    aTc: any
    bTc: any
    motors: hkpConstraintMotor
    switchBodies: bool
