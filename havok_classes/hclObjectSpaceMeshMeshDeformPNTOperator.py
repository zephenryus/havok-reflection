from .hclObjectSpaceMeshMeshDeformOperator import hclObjectSpaceMeshMeshDeformOperator
from .hclObjectSpaceDeformerLocalBlockPNT import hclObjectSpaceDeformerLocalBlockPNT
from .hclObjectSpaceDeformerLocalBlockUnpackedPNT import hclObjectSpaceDeformerLocalBlockUnpackedPNT


class hclObjectSpaceMeshMeshDeformPNTOperator(hclObjectSpaceMeshMeshDeformOperator):
    localPNTs: hclObjectSpaceDeformerLocalBlockPNT
    localUnpackedPNTs: hclObjectSpaceDeformerLocalBlockUnpackedPNT

    def __init__(self, infile):
        self.localPNTs = hclObjectSpaceDeformerLocalBlockPNT(infile)  # TYPE_ARRAY
        self.localUnpackedPNTs = hclObjectSpaceDeformerLocalBlockUnpackedPNT(infile)  # TYPE_ARRAY
