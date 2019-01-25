from .hclConstraintSet import hclConstraintSet
from typing import List
from .common import get_array
from .hclBendStiffnessConstraintSetMxBatch import hclBendStiffnessConstraintSetMxBatch
from .hclBendStiffnessConstraintSetMxSingle import hclBendStiffnessConstraintSetMxSingle
import struct


class hclBendStiffnessConstraintSetMx(hclConstraintSet):
    batches: List[hclBendStiffnessConstraintSetMxBatch]
    singles: List[hclBendStiffnessConstraintSetMxSingle]
    useRestPoseConfig: bool

    def __init__(self, infile):
        self.batches = get_array(infile, hclBendStiffnessConstraintSetMxBatch, 0)  # TYPE_ARRAY:TYPE_STRUCT
        self.singles = get_array(infile, hclBendStiffnessConstraintSetMxSingle, 0)  # TYPE_ARRAY:TYPE_STRUCT
        self.useRestPoseConfig = struct.unpack('>?', infile.read(1))  # TYPE_BOOL:TYPE_VOID

    def __repr__(self):
        return "<{class_name} batches=[{batches}], singles=[{singles}], useRestPoseConfig={useRestPoseConfig}>".format(**{
            "class_name": self.__class__.__name__,
            "batches": self.batches,
            "singles": self.singles,
            "useRestPoseConfig": self.useRestPoseConfig,
        })
