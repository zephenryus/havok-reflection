from .hclConstraintSet import hclConstraintSet
from enum import Enum
from typing import List
from .common import get_array
from .hclLocalRangeConstraintSetLocalConstraint import hclLocalRangeConstraintSetLocalConstraint
import struct
from .enums import ShapeType


class ShapeType(Enum):
    SHAPE_SPHERE = 0
    SHAPE_CYLINDER = 1


class ForceUpgrade6(Enum):
    HCL_FORCE_UPGRADE6 = 0


class hclLocalRangeConstraintSet(hclConstraintSet):
    localConstraints: List[hclLocalRangeConstraintSetLocalConstraint]
    referenceMeshBufferIdx: int
    stiffness: float
    shapeType: ShapeType
    applyNormalComponent: bool

    def __init__(self, infile):
        self.localConstraints = get_array(infile, hclLocalRangeConstraintSetLocalConstraint, 0)  # TYPE_ARRAY:TYPE_STRUCT
        self.referenceMeshBufferIdx = struct.unpack('>I', infile.read(4))  # TYPE_UINT32:TYPE_VOID
        self.stiffness = struct.unpack('>f', infile.read(4))  # TYPE_REAL:TYPE_VOID
        self.shapeType = ShapeType(infile)  # TYPE_ENUM:TYPE_UINT32
        self.applyNormalComponent = struct.unpack('>?', infile.read(1))  # TYPE_BOOL:TYPE_VOID

    def __repr__(self):
        return "<{class_name} localConstraints=[{localConstraints}], referenceMeshBufferIdx={referenceMeshBufferIdx}, stiffness={stiffness}, shapeType={shapeType}, applyNormalComponent={applyNormalComponent}>".format(**{
            "class_name": self.__class__.__name__,
            "localConstraints": self.localConstraints,
            "referenceMeshBufferIdx": self.referenceMeshBufferIdx,
            "stiffness": self.stiffness,
            "shapeType": self.shapeType,
            "applyNormalComponent": self.applyNormalComponent,
        })
