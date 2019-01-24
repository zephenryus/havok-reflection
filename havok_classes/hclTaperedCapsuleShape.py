from .hclShape import hclShape
from .common import vector4


class hclTaperedCapsuleShape(hclShape):
    small: vector4
    big: vector4
    coneApex: vector4
    coneAxis: vector4
    lVec: vector4
    dVec: vector4
    tanThetaVecNeg: vector4
    smallRadius: float
    bigRadius: float
    l: float
    d: float
    cosTheta: float
    sinTheta: float
    tanTheta: float
    tanThetaSqr: float
