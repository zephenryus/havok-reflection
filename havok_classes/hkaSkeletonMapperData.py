from enum import Enum
from .hkaSkeleton import hkaSkeleton
from .common import any
from .hkaSkeletonMapperDataPartitionMappingRange import hkaSkeletonMapperDataPartitionMappingRange
from .hkaSkeletonMapperDataSimpleMapping import hkaSkeletonMapperDataSimpleMapping
from .hkaSkeletonMapperDataChainMapping import hkaSkeletonMapperDataChainMapping
import struct
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

    def __init__(self, infile):
        self.skeletonA = hkaSkeleton(infile)  # TYPE_POINTER
        self.skeletonB = hkaSkeleton(infile)  # TYPE_POINTER
        self.partitionMap = any(infile)  # TYPE_ARRAY
        self.simpleMappingPartitionRanges = hkaSkeletonMapperDataPartitionMappingRange(infile)  # TYPE_ARRAY
        self.chainMappingPartitionRanges = hkaSkeletonMapperDataPartitionMappingRange(infile)  # TYPE_ARRAY
        self.simpleMappings = hkaSkeletonMapperDataSimpleMapping(infile)  # TYPE_ARRAY
        self.chainMappings = hkaSkeletonMapperDataChainMapping(infile)  # TYPE_ARRAY
        self.unmappedBones = any(infile)  # TYPE_ARRAY
        self.extractedMotionMapping = any(infile)  # TYPE_QSTRANSFORM
        self.keepUnmappedLocal = struct.unpack('>?', infile.read(1))
        self.mappingType = MappingType(infile)  # TYPE_ENUM
