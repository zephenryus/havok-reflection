from .hclBoneSpaceSkinOperator import hclBoneSpaceSkinOperator
from .hclBoneSpaceDeformerLocalBlockP import hclBoneSpaceDeformerLocalBlockP
from .hclBoneSpaceDeformerLocalBlockUnpackedP import hclBoneSpaceDeformerLocalBlockUnpackedP


class hclBoneSpaceSkinPOperator(hclBoneSpaceSkinOperator):
    localPs: hclBoneSpaceDeformerLocalBlockP
    localUnpackedPs: hclBoneSpaceDeformerLocalBlockUnpackedP

    def __init__(self, infile):
        self.localPs = hclBoneSpaceDeformerLocalBlockP(infile)  # TYPE_ARRAY
        self.localUnpackedPs = hclBoneSpaceDeformerLocalBlockUnpackedP(infile)  # TYPE_ARRAY
