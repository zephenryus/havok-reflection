from .common import vector4


class hclSimClothDataOverridableSimulationInfo(object):
    gravity: vector4
    globalDampingPerSecond: float
    collisionTolerance: float
    subSteps: int
    pinchDetectionEnabled: bool
    landscapeCollisionEnabled: bool
    transferMotionEnabled: bool
