from .hclObjectSpaceSkinOperator import hclObjectSpaceSkinOperator
from .hclObjectSpaceDeformerLocalBlockPNTB import hclObjectSpaceDeformerLocalBlockPNTB
from .hclObjectSpaceDeformerLocalBlockUnpackedPNTB import hclObjectSpaceDeformerLocalBlockUnpackedPNTB


class hclObjectSpaceSkinPNTBOperator(hclObjectSpaceSkinOperator):
    localPNTBs: hclObjectSpaceDeformerLocalBlockPNTB
    localUnpackedPNTBs: hclObjectSpaceDeformerLocalBlockUnpackedPNTB

    def __init__(self, infile):
        self.localPNTBs = hclObjectSpaceDeformerLocalBlockPNTB(infile)  # TYPE_ARRAY
        self.localUnpackedPNTBs = hclObjectSpaceDeformerLocalBlockUnpackedPNTB(infile)  # TYPE_ARRAY
