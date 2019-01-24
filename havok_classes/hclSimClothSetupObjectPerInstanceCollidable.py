from .hclCollidable import hclCollidable
from .hclVertexSelectionInput import hclVertexSelectionInput


class hclSimClothSetupObjectPerInstanceCollidable(object):
    collidable: hclCollidable
    collidingParticles: hclVertexSelectionInput
    drivingBoneName: str
    pinchDetectionEnabled: bool
    pinchDetectionPriority: int
    pinchDetectionRadius: float
