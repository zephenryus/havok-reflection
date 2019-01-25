from enum import Enum
from .hclBoneSpaceDeformerFourBlendEntryBlock import hclBoneSpaceDeformerFourBlendEntryBlock
from .hclBoneSpaceDeformerThreeBlendEntryBlock import hclBoneSpaceDeformerThreeBlendEntryBlock
from .hclBoneSpaceDeformerTwoBlendEntryBlock import hclBoneSpaceDeformerTwoBlendEntryBlock
from .hclBoneSpaceDeformerOneBlendEntryBlock import hclBoneSpaceDeformerOneBlendEntryBlock
from .common import any
import struct


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

    def __init__(self, infile):
        self.fourBlendEntries = hclBoneSpaceDeformerFourBlendEntryBlock(infile)  # TYPE_ARRAY
        self.threeBlendEntries = hclBoneSpaceDeformerThreeBlendEntryBlock(infile)  # TYPE_ARRAY
        self.twoBlendEntries = hclBoneSpaceDeformerTwoBlendEntryBlock(infile)  # TYPE_ARRAY
        self.oneBlendEntries = hclBoneSpaceDeformerOneBlendEntryBlock(infile)  # TYPE_ARRAY
        self.controlBytes = any(infile)  # TYPE_ARRAY
        self.startVertexIndex = struct.unpack('>H', infile.read(2))
        self.endVertexIndex = struct.unpack('>H', infile.read(2))
        self.batchSizeSpu = struct.unpack('>H', infile.read(2))
        self.partialWrite = struct.unpack('>?', infile.read(1))
