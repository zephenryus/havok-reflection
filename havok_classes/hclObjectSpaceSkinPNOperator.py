from .hclObjectSpaceSkinOperator import hclObjectSpaceSkinOperator
from .hclObjectSpaceDeformerLocalBlockPN import hclObjectSpaceDeformerLocalBlockPN
from .hclObjectSpaceDeformerLocalBlockUnpackedPN import hclObjectSpaceDeformerLocalBlockUnpackedPN


class hclObjectSpaceSkinPNOperator(hclObjectSpaceSkinOperator):
    localPNs: hclObjectSpaceDeformerLocalBlockPN
    localUnpackedPNs: hclObjectSpaceDeformerLocalBlockUnpackedPN

    def __init__(self, infile):
        self.localPNs = hclObjectSpaceDeformerLocalBlockPN(infile)  # TYPE_ARRAY
        self.localUnpackedPNs = hclObjectSpaceDeformerLocalBlockUnpackedPN(infile)  # TYPE_ARRAY
