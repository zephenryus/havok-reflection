from .hclObjectSpaceMeshMeshDeformOperator import hclObjectSpaceMeshMeshDeformOperator
from .hclObjectSpaceDeformerLocalBlockP import hclObjectSpaceDeformerLocalBlockP
from .hclObjectSpaceDeformerLocalBlockUnpackedP import hclObjectSpaceDeformerLocalBlockUnpackedP


class hclObjectSpaceMeshMeshDeformPOperator(hclObjectSpaceMeshMeshDeformOperator):
    localPs: hclObjectSpaceDeformerLocalBlockP
    localUnpackedPs: hclObjectSpaceDeformerLocalBlockUnpackedP

    def __init__(self, infile):
        self.localPs = hclObjectSpaceDeformerLocalBlockP(infile)  # TYPE_ARRAY
        self.localUnpackedPs = hclObjectSpaceDeformerLocalBlockUnpackedP(infile)  # TYPE_ARRAY
