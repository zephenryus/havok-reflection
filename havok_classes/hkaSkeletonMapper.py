from .hkReferencedObject import hkReferencedObject
from enum import Enum
from .hkaSkeletonMapperData import hkaSkeletonMapperData


class ConstraintSource(Enum):
    NO_CONSTRAINTS = 0
    REFERENCE_POSE = 1
    CURRENT_POSE = 2


class hkaSkeletonMapper(hkReferencedObject):
    mapping: hkaSkeletonMapperData

    def __init__(self, infile):
        self.mapping = hkaSkeletonMapperData(infile)  # TYPE_STRUCT:TYPE_VOID

    def __repr__(self):
        return "<{class_name} mapping={mapping}>".format(**{
            "class_name": self.__class__.__name__,
            "mapping": self.mapping,
        })
