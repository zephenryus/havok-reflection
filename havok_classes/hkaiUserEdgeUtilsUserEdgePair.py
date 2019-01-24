from .common import vector4
from .enums import UserEdgeDirection


class hkaiUserEdgeUtilsUserEdgePair(object):
    x: vector4
    y: vector4
    z: vector4
    instanceUidA: int
    instanceUidB: int
    faceA: int
    faceB: int
    userDataA: int
    userDataB: int
    costAtoB: int
    costBtoA: int
    direction: UserEdgeDirection
