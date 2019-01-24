from enum import Enum
from .hkaSkeleton import hkaSkeleton
from .common import any
from .hkaSkeletonMapperDataPartitionMappingRange import hkaSkeletonMapperDataPartitionMappingRange
from .hkaSkeletonMapperDataSimpleMapping import hkaSkeletonMapperDataSimpleMapping
from .hkaSkeletonMapperDataChainMapping import hkaSkeletonMapperDataChainMapping
from .enums import MappingType


class MappingType(Enum):
    HK_RAGDOLL_MAPPING = 0
    HK_RETARGETING_MAPPING = 1


class hkaSkeletonMapperData(object):
    skeletonA: hkaSkeleton
    skeletonB: hkaSkeleton
    partitionMap: any
    simpleMappingPartitionRanges: hkaSkeletonMapperDataPartitionMappingRange
    chainMappingPartitionRanges: hkaSkeletonMapperDataPartitionMappingRange
    simpleMappings: hkaSkeletonMapperDataSimpleMapping
    chainMappings: hkaSkeletonMapperDataChainMapping
    unmappedBones: any
    extractedMotionMapping: any
    keepUnmappedLocal: bool
    mappingType: MappingType
