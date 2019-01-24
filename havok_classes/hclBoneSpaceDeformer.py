from enum import Enum
from .hclBoneSpaceDeformerFourBlendEntryBlock import hclBoneSpaceDeformerFourBlendEntryBlock
from .hclBoneSpaceDeformerThreeBlendEntryBlock import hclBoneSpaceDeformerThreeBlendEntryBlock
from .hclBoneSpaceDeformerTwoBlendEntryBlock import hclBoneSpaceDeformerTwoBlendEntryBlock
from .hclBoneSpaceDeformerOneBlendEntryBlock import hclBoneSpaceDeformerOneBlendEntryBlock
from .common import any


class ControlByte(Enum):
    FOUR_BLEND = 0
    THREE_BLEND = 1
    TWO_BLEND = 2
    ONE_BLEND = 3
    NEXT_SPU_BATCH = 4


class hclBoneSpaceDeformer(object):
    fourBlendEntries: hclBoneSpaceDeformerFourBlendEntryBlock
    threeBlendEntries: hclBoneSpaceDeformerThreeBlendEntryBlock
    twoBlendEntries: hclBoneSpaceDeformerTwoBlendEntryBlock
    oneBlendEntries: hclBoneSpaceDeformerOneBlendEntryBlock
    controlBytes: any
    startVertexIndex: int
    endVertexIndex: int
    batchSizeSpu: int
    partialWrite: bool
