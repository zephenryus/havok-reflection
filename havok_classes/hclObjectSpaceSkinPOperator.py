from .hclObjectSpaceSkinOperator import hclObjectSpaceSkinOperator
from .hclObjectSpaceDeformerLocalBlockP import hclObjectSpaceDeformerLocalBlockP
from .hclObjectSpaceDeformerLocalBlockUnpackedP import hclObjectSpaceDeformerLocalBlockUnpackedP


class hclObjectSpaceSkinPOperator(hclObjectSpaceSkinOperator):
    localPs: hclObjectSpaceDeformerLocalBlockP
    localUnpackedPs: hclObjectSpaceDeformerLocalBlockUnpackedP

    def __init__(self, infile):
        self.localPs = hclObjectSpaceDeformerLocalBlockP(infile)  # TYPE_ARRAY
        self.localUnpackedPs = hclObjectSpaceDeformerLocalBlockUnpackedP(infile)  # TYPE_ARRAY
