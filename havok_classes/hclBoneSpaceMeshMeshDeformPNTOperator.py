from .hclBoneSpaceMeshMeshDeformOperator import hclBoneSpaceMeshMeshDeformOperator
from .hclBoneSpaceDeformerLocalBlockPNT import hclBoneSpaceDeformerLocalBlockPNT
from .hclBoneSpaceDeformerLocalBlockUnpackedPNT import hclBoneSpaceDeformerLocalBlockUnpackedPNT


class hclBoneSpaceMeshMeshDeformPNTOperator(hclBoneSpaceMeshMeshDeformOperator):
    localPNTs: hclBoneSpaceDeformerLocalBlockPNT
    localUnpackedPNTs: hclBoneSpaceDeformerLocalBlockUnpackedPNT

    def __init__(self, infile):
        self.localPNTs = hclBoneSpaceDeformerLocalBlockPNT(infile)  # TYPE_ARRAY
        self.localUnpackedPNTs = hclBoneSpaceDeformerLocalBlockUnpackedPNT(infile)  # TYPE_ARRAY
