from .hclObjectSpaceSkinOperator import hclObjectSpaceSkinOperator
from .hclObjectSpaceDeformerLocalBlockPNTB import hclObjectSpaceDeformerLocalBlockPNTB
from .hclObjectSpaceDeformerLocalBlockUnpackedPNTB import hclObjectSpaceDeformerLocalBlockUnpackedPNTB


class hclObjectSpaceSkinPNTBOperator(hclObjectSpaceSkinOperator):
    localPNTBs: hclObjectSpaceDeformerLocalBlockPNTB
    localUnpackedPNTBs: hclObjectSpaceDeformerLocalBlockUnpackedPNTB
