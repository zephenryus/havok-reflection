from .hkReferencedObject import hkReferencedObject
from enum import Enum
from .hkaSkeletonMapperData import hkaSkeletonMapperData


class ConstraintSource(Enum):
    NO_CONSTRAINTS = 0
    REFERENCE_POSE = 1
    CURRENT_POSE = 2


class hkaSkeletonMapper(hkReferencedObject):
    mapping: hkaSkeletonMapperData
