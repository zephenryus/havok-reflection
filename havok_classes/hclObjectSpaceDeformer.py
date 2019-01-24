from enum import Enum
from .hclObjectSpaceDeformerEightBlendEntryBlock import hclObjectSpaceDeformerEightBlendEntryBlock
from .hclObjectSpaceDeformerSevenBlendEntryBlock import hclObjectSpaceDeformerSevenBlendEntryBlock
from .hclObjectSpaceDeformerSixBlendEntryBlock import hclObjectSpaceDeformerSixBlendEntryBlock
from .hclObjectSpaceDeformerFiveBlendEntryBlock import hclObjectSpaceDeformerFiveBlendEntryBlock
from .hclObjectSpaceDeformerFourBlendEntryBlock import hclObjectSpaceDeformerFourBlendEntryBlock
from .hclObjectSpaceDeformerThreeBlendEntryBlock import hclObjectSpaceDeformerThreeBlendEntryBlock
from .hclObjectSpaceDeformerTwoBlendEntryBlock import hclObjectSpaceDeformerTwoBlendEntryBlock
from .hclObjectSpaceDeformerOneBlendEntryBlock import hclObjectSpaceDeformerOneBlendEntryBlock
from .common import any


class ControlByte(Enum):
    FOUR_BLEND = 0
    THREE_BLEND = 1
    TWO_BLEND = 2
    ONE_BLEND = 3
    NEXT_SPU_BATCH = 4
    EIGHT_BLEND = 5
    SEVEN_BLEND = 6
    SIX_BLEND = 7
    FIVE_BLEND = 8


class hclObjectSpaceDeformer(object):
    eightBlendEntries: hclObjectSpaceDeformerEightBlendEntryBlock
    sevenBlendEntries: hclObjectSpaceDeformerSevenBlendEntryBlock
    sixBlendEntries: hclObjectSpaceDeformerSixBlendEntryBlock
    fiveBlendEntries: hclObjectSpaceDeformerFiveBlendEntryBlock
    fourBlendEntries: hclObjectSpaceDeformerFourBlendEntryBlock
    threeBlendEntries: hclObjectSpaceDeformerThreeBlendEntryBlock
    twoBlendEntries: hclObjectSpaceDeformerTwoBlendEntryBlock
    oneBlendEntries: hclObjectSpaceDeformerOneBlendEntryBlock
    controlBytes: any
    startVertexIndex: int
    endVertexIndex: int
    batchSizeSpu: int
    partialWrite: bool
