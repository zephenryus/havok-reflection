from .hclBoneSpaceSkinOperator import hclBoneSpaceSkinOperator
from .hclBoneSpaceDeformerLocalBlockPN import hclBoneSpaceDeformerLocalBlockPN
from .hclBoneSpaceDeformerLocalBlockUnpackedPN import hclBoneSpaceDeformerLocalBlockUnpackedPN


class hclBoneSpaceSkinPNOperator(hclBoneSpaceSkinOperator):
    localPNs: hclBoneSpaceDeformerLocalBlockPN
    localUnpackedPNs: hclBoneSpaceDeformerLocalBlockUnpackedPN

    def __init__(self, infile):
        self.localPNs = hclBoneSpaceDeformerLocalBlockPN(infile)  # TYPE_ARRAY
        self.localUnpackedPNs = hclBoneSpaceDeformerLocalBlockUnpackedPN(infile)  # TYPE_ARRAY
