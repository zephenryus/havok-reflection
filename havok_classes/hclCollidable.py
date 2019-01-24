from .hkReferencedObject import hkReferencedObject
from .common import any, vector4
from .hclShape import hclShape


class hclCollidable(hkReferencedObject):
    name: str
    transform: any
    linearVelocity: vector4
    angularVelocity: vector4
    pinchDetectionEnabled: bool
    pinchDetectionPriority: int
    pinchDetectionRadius: float
    shape: hclShape
