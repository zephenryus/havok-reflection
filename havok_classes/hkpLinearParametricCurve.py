from .hkpParametricCurve import hkpParametricCurve
from .common import vector4, any


class hkpLinearParametricCurve(hkpParametricCurve):
    smoothingFactor: float
    closedLoop: bool
    dirNotParallelToTangentAlongWholePath: vector4
    points: any
    distance: any
