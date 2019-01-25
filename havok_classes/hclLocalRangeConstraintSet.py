from .hclConstraintSet import hclConstraintSet
from enum import Enum
from .hclLocalRangeConstraintSetLocalConstraint import hclLocalRangeConstraintSetLocalConstraint
import struct
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

    def __init__(self, infile):
        self.localConstraints = hclLocalRangeConstraintSetLocalConstraint(infile)  # TYPE_ARRAY
        self.referenceMeshBufferIdx = struct.unpack('>I', infile.read(4))
        self.stiffness = struct.unpack('>f', infile.read(4))
        self.shapeType = ShapeType(infile)  # TYPE_ENUM
        self.applyNormalComponent = struct.unpack('>?', infile.read(1))
