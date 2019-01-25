from .hclBoneSpaceMeshMeshDeformOperator import hclBoneSpaceMeshMeshDeformOperator
from .hclBoneSpaceDeformerLocalBlockPNTB import hclBoneSpaceDeformerLocalBlockPNTB
from .hclBoneSpaceDeformerLocalBlockUnpackedPNTB import hclBoneSpaceDeformerLocalBlockUnpackedPNTB


class hclBoneSpaceMeshMeshDeformPNTBOperator(hclBoneSpaceMeshMeshDeformOperator):
    localPNTBs: hclBoneSpaceDeformerLocalBlockPNTB
    localUnpackedPNTBs: hclBoneSpaceDeformerLocalBlockUnpackedPNTB

    def __init__(self, infile):
        self.localPNTBs = hclBoneSpaceDeformerLocalBlockPNTB(infile)  # TYPE_ARRAY
        self.localUnpackedPNTBs = hclBoneSpaceDeformerLocalBlockUnpackedPNTB(infile)  # TYPE_ARRAY
