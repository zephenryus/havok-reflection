from enum import Enum
from typing import List
from .common import get_array
from .hclBoneSpaceDeformerFourBlendEntryBlock import hclBoneSpaceDeformerFourBlendEntryBlock
from .hclBoneSpaceDeformerThreeBlendEntryBlock import hclBoneSpaceDeformerThreeBlendEntryBlock
from .hclBoneSpaceDeformerTwoBlendEntryBlock import hclBoneSpaceDeformerTwoBlendEntryBlock
from .hclBoneSpaceDeformerOneBlendEntryBlock import hclBoneSpaceDeformerOneBlendEntryBlock
import struct


class ControlByte(Enum):
    FOUR_BLEND = 0
    THREE_BLEND = 1
    TWO_BLEND = 2
    ONE_BLEND = 3
    NEXT_SPU_BATCH = 4


class hclBoneSpaceDeformer(object):
    fourBlendEntries: List[hclBoneSpaceDeformerFourBlendEntryBlock]
    threeBlendEntries: List[hclBoneSpaceDeformerThreeBlendEntryBlock]
    twoBlendEntries: List[hclBoneSpaceDeformerTwoBlendEntryBlock]
    oneBlendEntries: List[hclBoneSpaceDeformerOneBlendEntryBlock]
    controlBytes: List[int]
    startVertexIndex: int
    endVertexIndex: int
    batchSizeSpu: int
    partialWrite: bool

    def __init__(self, infile):
        self.fourBlendEntries = get_array(infile, hclBoneSpaceDeformerFourBlendEntryBlock, 0)  # TYPE_ARRAY:TYPE_STRUCT
        self.threeBlendEntries = get_array(infile, hclBoneSpaceDeformerThreeBlendEntryBlock, 0)  # TYPE_ARRAY:TYPE_STRUCT
        self.twoBlendEntries = get_array(infile, hclBoneSpaceDeformerTwoBlendEntryBlock, 0)  # TYPE_ARRAY:TYPE_STRUCT
        self.oneBlendEntries = get_array(infile, hclBoneSpaceDeformerOneBlendEntryBlock, 0)  # TYPE_ARRAY:TYPE_STRUCT
        self.controlBytes = get_array(infile, int, 1)  # TYPE_ARRAY:TYPE_UINT8
        self.startVertexIndex = struct.unpack('>H', infile.read(2))  # TYPE_UINT16:TYPE_VOID
        self.endVertexIndex = struct.unpack('>H', infile.read(2))  # TYPE_UINT16:TYPE_VOID
        self.batchSizeSpu = struct.unpack('>H', infile.read(2))  # TYPE_UINT16:TYPE_VOID
        self.partialWrite = struct.unpack('>?', infile.read(1))  # TYPE_BOOL:TYPE_VOID

    def __repr__(self):
        return "<{class_name} fourBlendEntries=[{fourBlendEntries}], threeBlendEntries=[{threeBlendEntries}], twoBlendEntries=[{twoBlendEntries}], oneBlendEntries=[{oneBlendEntries}], controlBytes=[{controlBytes}], startVertexIndex={startVertexIndex}, endVertexIndex={endVertexIndex}, batchSizeSpu={batchSizeSpu}, partialWrite={partialWrite}>".format(**{
            "class_name": self.__class__.__name__,
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
