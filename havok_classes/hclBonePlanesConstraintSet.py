from .hclConstraintSet import hclConstraintSet
from .hclBonePlanesConstraintSetBonePlane import hclBonePlanesConstraintSetBonePlane


class hclBonePlanesConstraintSet(hclConstraintSet):
    bonePlanes: hclBonePlanesConstraintSetBonePlane
    transformSetIndex: int
