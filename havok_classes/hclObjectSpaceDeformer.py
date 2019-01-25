from enum import Enum
from typing import List
from .common import get_array
from .hclObjectSpaceDeformerEightBlendEntryBlock import hclObjectSpaceDeformerEightBlendEntryBlock
from .hclObjectSpaceDeformerSevenBlendEntryBlock import hclObjectSpaceDeformerSevenBlendEntryBlock
from .hclObjectSpaceDeformerSixBlendEntryBlock import hclObjectSpaceDeformerSixBlendEntryBlock
from .hclObjectSpaceDeformerFiveBlendEntryBlock import hclObjectSpaceDeformerFiveBlendEntryBlock
from .hclObjectSpaceDeformerFourBlendEntryBlock import hclObjectSpaceDeformerFourBlendEntryBlock
from .hclObjectSpaceDeformerThreeBlendEntryBlock import hclObjectSpaceDeformerThreeBlendEntryBlock
from .hclObjectSpaceDeformerTwoBlendEntryBlock import hclObjectSpaceDeformerTwoBlendEntryBlock
from .hclObjectSpaceDeformerOneBlendEntryBlock import hclObjectSpaceDeformerOneBlendEntryBlock
import struct


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
    eightBlendEntries: List[hclObjectSpaceDeformerEightBlendEntryBlock]
    sevenBlendEntries: List[hclObjectSpaceDeformerSevenBlendEntryBlock]
    sixBlendEntries: List[hclObjectSpaceDeformerSixBlendEntryBlock]
    fiveBlendEntries: List[hclObjectSpaceDeformerFiveBlendEntryBlock]
    fourBlendEntries: List[hclObjectSpaceDeformerFourBlendEntryBlock]
    threeBlendEntries: List[hclObjectSpaceDeformerThreeBlendEntryBlock]
    twoBlendEntries: List[hclObjectSpaceDeformerTwoBlendEntryBlock]
    oneBlendEntries: List[hclObjectSpaceDeformerOneBlendEntryBlock]
    controlBytes: List[int]
    startVertexIndex: int
    endVertexIndex: int
    batchSizeSpu: int
    partialWrite: bool

    def __init__(self, infile):
        self.eightBlendEntries = get_array(infile, hclObjectSpaceDeformerEightBlendEntryBlock, 0)  # TYPE_ARRAY:TYPE_STRUCT
        self.sevenBlendEntries = get_array(infile, hclObjectSpaceDeformerSevenBlendEntryBlock, 0)  # TYPE_ARRAY:TYPE_STRUCT
        self.sixBlendEntries = get_array(infile, hclObjectSpaceDeformerSixBlendEntryBlock, 0)  # TYPE_ARRAY:TYPE_STRUCT
        self.fiveBlendEntries = get_array(infile, hclObjectSpaceDeformerFiveBlendEntryBlock, 0)  # TYPE_ARRAY:TYPE_STRUCT
        self.fourBlendEntries = get_array(infile, hclObjectSpaceDeformerFourBlendEntryBlock, 0)  # TYPE_ARRAY:TYPE_STRUCT
        self.threeBlendEntries = get_array(infile, hclObjectSpaceDeformerThreeBlendEntryBlock, 0)  # TYPE_ARRAY:TYPE_STRUCT
        self.twoBlendEntries = get_array(infile, hclObjectSpaceDeformerTwoBlendEntryBlock, 0)  # TYPE_ARRAY:TYPE_STRUCT
        self.oneBlendEntries = get_array(infile, hclObjectSpaceDeformerOneBlendEntryBlock, 0)  # TYPE_ARRAY:TYPE_STRUCT
        self.controlBytes = get_array(infile, int, 1)  # TYPE_ARRAY:TYPE_UINT8
        self.startVertexIndex = struct.unpack('>H', infile.read(2))  # TYPE_UINT16:TYPE_VOID
        self.endVertexIndex = struct.unpack('>H', infile.read(2))  # TYPE_UINT16:TYPE_VOID
        self.batchSizeSpu = struct.unpack('>H', infile.read(2))  # TYPE_UINT16:TYPE_VOID
        self.partialWrite = struct.unpack('>?', infile.read(1))  # TYPE_BOOL:TYPE_VOID

    def __repr__(self):
        return "<{class_name} eightBlendEntries=[{eightBlendEntries}], sevenBlendEntries=[{sevenBlendEntries}], sixBlendEntries=[{sixBlendEntries}], fiveBlendEntries=[{fiveBlendEntries}], fourBlendEntries=[{fourBlendEntries}], threeBlendEntries=[{threeBlendEntries}], twoBlendEntries=[{twoBlendEntries}], oneBlendEntries=[{oneBlendEntries}], controlBytes=[{controlBytes}], startVertexIndex={startVertexIndex}, endVertexIndex={endVertexIndex}, batchSizeSpu={batchSizeSpu}, partialWrite={partialWrite}>".format(**{
            "class_name": self.__class__.__name__,
            "eightBlendEntries": self.eightBlendEntries,
            "sevenBlendEntries": self.sevenBlendEntries,
            "sixBlendEntries": self.sixBlendEntries,
            "fiveBlendEntries": self.fiveBlendEntries,
            "fourBlendEntries": self.fourBlendEntries,
            "threeBlendEntries": self.threeBlendEntries,
            "twoBlendEntries": self.twoBlendEntries,
            "oneBlendEntries": self.oneBlendEntries,
            "controlBytes": self.controlBytes,
            "startVertexIndex": self.startVertexIndex,
            "endVertexIndex": self.endVertexIndex,
            "batchSizeSpu": self.batchSizeSpu,
            "partialWrite": self.partialWrite,
        })
