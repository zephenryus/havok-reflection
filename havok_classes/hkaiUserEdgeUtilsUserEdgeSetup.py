from .hkaiUserEdgeUtilsObb import hkaiUserEdgeUtilsObb
from .common import vector4
from .enums import UserEdgeDirection, UserEdgeSetupSpace


class hkaiUserEdgeUtilsUserEdgeSetup(object):
    obbA: hkaiUserEdgeUtilsObb
    obbB: hkaiUserEdgeUtilsObb
    userDataA: int
    userDataB: int
    costAtoB: float
    costBtoA: float
    worldUpA: vector4
    worldUpB: vector4
    direction: UserEdgeDirection
    space: UserEdgeSetupSpace
    forceAlign: bool
