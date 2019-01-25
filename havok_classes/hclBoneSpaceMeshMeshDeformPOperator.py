from .hclBoneSpaceMeshMeshDeformOperator import hclBoneSpaceMeshMeshDeformOperator
from .hclBoneSpaceDeformerLocalBlockP import hclBoneSpaceDeformerLocalBlockP
from .hclBoneSpaceDeformerLocalBlockUnpackedP import hclBoneSpaceDeformerLocalBlockUnpackedP


class hclBoneSpaceMeshMeshDeformPOperator(hclBoneSpaceMeshMeshDeformOperator):
    localPs: hclBoneSpaceDeformerLocalBlockP
    localUnpackedPs: hclBoneSpaceDeformerLocalBlockUnpackedP

    def __init__(self, infile):
        self.localPs = hclBoneSpaceDeformerLocalBlockP(infile)  # TYPE_ARRAY
        self.localUnpackedPs = hclBoneSpaceDeformerLocalBlockUnpackedP(infile)  # TYPE_ARRAY
