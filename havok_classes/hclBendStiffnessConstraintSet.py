from .hclConstraintSet import hclConstraintSet
from .hclBendStiffnessConstraintSetLink import hclBendStiffnessConstraintSetLink
import struct


class hclBendStiffnessConstraintSet(hclConstraintSet):
    links: hclBendStiffnessConstraintSetLink
    useRestPoseConfig: bool

    def __init__(self, infile):
        self.links = hclBendStiffnessConstraintSetLink(infile)  # TYPE_ARRAY
        self.useRestPoseConfig = struct.unpack('>?', infile.read(1))
