from .hclObjectSpaceSkinOperator import hclObjectSpaceSkinOperator
from .hclObjectSpaceDeformerLocalBlockPNT import hclObjectSpaceDeformerLocalBlockPNT
from .hclObjectSpaceDeformerLocalBlockUnpackedPNT import hclObjectSpaceDeformerLocalBlockUnpackedPNT


class hclObjectSpaceSkinPNTOperator(hclObjectSpaceSkinOperator):
    localPNTs: hclObjectSpaceDeformerLocalBlockPNT
    localUnpackedPNTs: hclObjectSpaceDeformerLocalBlockUnpackedPNT

    def __init__(self, infile):
        self.localPNTs = hclObjectSpaceDeformerLocalBlockPNT(infile)  # TYPE_ARRAY
        self.localUnpackedPNTs = hclObjectSpaceDeformerLocalBlockUnpackedPNT(infile)  # TYPE_ARRAY
