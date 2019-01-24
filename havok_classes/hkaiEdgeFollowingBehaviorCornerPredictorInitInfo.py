from .common import vector4


class hkaiEdgeFollowingBehaviorCornerPredictorInitInfo(object):
    positionLocal: vector4
    forwardVectorLocal: vector4
    upLocal: vector4
    positionSectionIndex: int
    nextEdgeIndex: int
    nextIsLeft: bool
    hasInfo: bool
