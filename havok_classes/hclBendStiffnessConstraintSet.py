from .hclConstraintSet import hclConstraintSet
from typing import List
from .common import get_array
from .hclBendStiffnessConstraintSetLink import hclBendStiffnessConstraintSetLink
import struct


class hclBendStiffnessConstraintSet(hclConstraintSet):
    links: List[hclBendStiffnessConstraintSetLink]
    useRestPoseConfig: bool

    def __init__(self, infile):
        self.links = get_array(infile, hclBendStiffnessConstraintSetLink, 0)  # TYPE_ARRAY:TYPE_STRUCT
        self.useRestPoseConfig = struct.unpack('>?', infile.read(1))  # TYPE_BOOL:TYPE_VOID

    def __repr__(self):
        return "<{class_name} links=[{links}], useRestPoseConfig={useRestPoseConfig}>".format(**{
            "class_name": self.__class__.__name__,
            "links": self.links,
            "useRestPoseConfig": self.useRestPoseConfig,
        })
