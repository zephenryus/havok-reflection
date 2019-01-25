from .hclBoneSpaceSkinOperator import hclBoneSpaceSkinOperator
from .hclBoneSpaceDeformerLocalBlockPNT import hclBoneSpaceDeformerLocalBlockPNT
from .hclBoneSpaceDeformerLocalBlockUnpackedPNT import hclBoneSpaceDeformerLocalBlockUnpackedPNT


class hclBoneSpaceSkinPNTOperator(hclBoneSpaceSkinOperator):
    localPNTs: hclBoneSpaceDeformerLocalBlockPNT
    localUnpackedPNTs: hclBoneSpaceDeformerLocalBlockUnpackedPNT

    def __init__(self, infile):
        self.localPNTs = hclBoneSpaceDeformerLocalBlockPNT(infile)  # TYPE_ARRAY
        self.localUnpackedPNTs = hclBoneSpaceDeformerLocalBlockUnpackedPNT(infile)  # TYPE_ARRAY
