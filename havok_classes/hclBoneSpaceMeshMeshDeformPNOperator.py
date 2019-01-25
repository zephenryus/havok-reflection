from .hclBoneSpaceMeshMeshDeformOperator import hclBoneSpaceMeshMeshDeformOperator
from typing import List
from .common import get_array
from .hclBoneSpaceDeformerLocalBlockPN import hclBoneSpaceDeformerLocalBlockPN
from .hclBoneSpaceDeformerLocalBlockUnpackedPN import hclBoneSpaceDeformerLocalBlockUnpackedPN


class hclBoneSpaceMeshMeshDeformPNOperator(hclBoneSpaceMeshMeshDeformOperator):
    localPNs: List[hclBoneSpaceDeformerLocalBlockPN]
    localUnpackedPNs: List[hclBoneSpaceDeformerLocalBlockUnpackedPN]

    def __init__(self, infile):
        self.localPNs = get_array(infile, hclBoneSpaceDeformerLocalBlockPN, 0)  # TYPE_ARRAY:TYPE_STRUCT
        self.localUnpackedPNs = get_array(infile, hclBoneSpaceDeformerLocalBlockUnpackedPN, 0)  # TYPE_ARRAY:TYPE_STRUCT

    def __repr__(self):
        return "<{class_name} localPNs=[{localPNs}], localUnpackedPNs=[{localUnpackedPNs}]>".format(**{
            "class_name": self.__class__.__name__,
            "localPNs": self.localPNs,
            "localUnpackedPNs": self.localUnpackedPNs,
        })
