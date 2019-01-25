from enum import Enum
from .hkaSkeleton import hkaSkeleton
from typing import List
from .common import get_array
from .hkaSkeletonMapperDataPartitionMappingRange import hkaSkeletonMapperDataPartitionMappingRange
from .hkaSkeletonMapperDataSimpleMapping import hkaSkeletonMapperDataSimpleMapping
from .hkaSkeletonMapperDataChainMapping import hkaSkeletonMapperDataChainMapping
import struct
from .enums import MappingType


class MappingType(Enum):
    HK_RAGDOLL_MAPPING = 0
    HK_RETARGETING_MAPPING = 1


class hkaSkeletonMapperData(object):
    skeletonA: any
    skeletonB: any
    partitionMap: List[int]
    simpleMappingPartitionRanges: List[hkaSkeletonMapperDataPartitionMappingRange]
    chainMappingPartitionRanges: List[hkaSkeletonMapperDataPartitionMappingRange]
    simpleMappings: List[hkaSkeletonMapperDataSimpleMapping]
    chainMappings: List[hkaSkeletonMapperDataChainMapping]
    unmappedBones: List[int]
    extractedMotionMapping: any
    keepUnmappedLocal: bool
    mappingType: MappingType

    def __init__(self, infile):
        self.skeletonA = any(infile)  # TYPE_POINTER:TYPE_STRUCT
        self.skeletonB = any(infile)  # TYPE_POINTER:TYPE_STRUCT
        self.partitionMap = get_array(infile, int, 2)  # TYPE_ARRAY:TYPE_INT16
        self.simpleMappingPartitionRanges = get_array(infile, hkaSkeletonMapperDataPartitionMappingRange, 0)  # TYPE_ARRAY:TYPE_STRUCT
        self.chainMappingPartitionRanges = get_array(infile, hkaSkeletonMapperDataPartitionMappingRange, 0)  # TYPE_ARRAY:TYPE_STRUCT
        self.simpleMappings = get_array(infile, hkaSkeletonMapperDataSimpleMapping, 0)  # TYPE_ARRAY:TYPE_STRUCT
        self.chainMappings = get_array(infile, hkaSkeletonMapperDataChainMapping, 0)  # TYPE_ARRAY:TYPE_STRUCT
        self.unmappedBones = get_array(infile, int, 2)  # TYPE_ARRAY:TYPE_INT16
        self.extractedMotionMapping = any(infile)  # TYPE_QSTRANSFORM:TYPE_VOID
        self.keepUnmappedLocal = struct.unpack('>?', infile.read(1))  # TYPE_BOOL:TYPE_VOID
        self.mappingType = MappingType(infile)  # TYPE_ENUM:TYPE_INT32

    def __repr__(self):
        return "<{class_name} skeletonA={skeletonA}, skeletonB={skeletonB}, partitionMap=[{partitionMap}], simpleMappingPartitionRanges=[{simpleMappingPartitionRanges}], chainMappingPartitionRanges=[{chainMappingPartitionRanges}], simpleMappings=[{simpleMappings}], chainMappings=[{chainMappings}], unmappedBones=[{unmappedBones}], extractedMotionMapping={extractedMotionMapping}, keepUnmappedLocal={keepUnmappedLocal}, mappingType={mappingType}>".format(**{
            "class_name": self.__class__.__name__,
            "skeletonA": self.skeletonA,
            "skeletonB": self.skeletonB,
            "partitionMap": self.partitionMap,
            "simpleMappingPartitionRanges": self.simpleMappingPartitionRanges,
            "chainMappingPartitionRanges": self.chainMappingPartitionRanges,
            "simpleMappings": self.simpleMappings,
            "chainMappings": self.chainMappings,
            "unmappedBones": self.unmappedBones,
            "extractedMotionMapping": self.extractedMotionMapping,
            "keepUnmappedLocal": self.keepUnmappedLocal,
            "mappingType": self.mappingType,
        })
