from .hclConstraintSet import hclConstraintSet
from .hclBendStiffnessConstraintSetMxBatch import hclBendStiffnessConstraintSetMxBatch
from .hclBendStiffnessConstraintSetMxSingle import hclBendStiffnessConstraintSetMxSingle
import struct


class hclBendStiffnessConstraintSetMx(hclConstraintSet):
    batches: hclBendStiffnessConstraintSetMxBatch
    singles: hclBendStiffnessConstraintSetMxSingle
    useRestPoseConfig: bool

    def __init__(self, infile):
        self.batches = hclBendStiffnessConstraintSetMxBatch(infile)  # TYPE_ARRAY
        self.singles = hclBendStiffnessConstraintSetMxSingle(infile)  # TYPE_ARRAY
        self.useRestPoseConfig = struct.unpack('>?', infile.read(1))
