from .hclConstraintSet import hclConstraintSet
from enum import Enum
from .hclLocalRangeConstraintSetLocalConstraint import hclLocalRangeConstraintSetLocalConstraint
from .enums import ShapeType


class ShapeType(Enum):
    SHAPE_SPHERE = 0
    SHAPE_CYLINDER = 1


class ForceUpgrade6(Enum):
    HCL_FORCE_UPGRADE6 = 0


class hclLocalRangeConstraintSet(hclConstraintSet):
    localConstraints: hclLocalRangeConstraintSetLocalConstraint
    referenceMeshBufferIdx: int
    stiffness: float
    shapeType: ShapeType
    applyNormalComponent: bool
