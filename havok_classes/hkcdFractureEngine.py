from .hkReferencedObject import hkReferencedObject
from enum import Enum


class SplitResult(Enum):
    SPLIT_SUCCESS = 0
    SPLIT_FAILURE = 1
    SPLIT_FAILURE_INSIDE = 2
    SPLIT_FAILURE_OUTSIDE = 3


class Type(Enum):
    TYPE_EXACT = 0
    TYPE_USER_0 = 16


class ExecutionFlagValues(Enum):
    CREATE_PHYSICS_SHAPES = 1
    CREATE_GRAPHICS_SHAPES = 2
    RECOMPUTE_INSIDE_TRANSFORM = 4
    RECOMPUTE_OUTSIDE_TRANSFORM = 8
    COMPUTE_INSIDE_SHAPES = 16
    COMPUTE_OUTSIDE_SHAPES = 32
    FRACTURE_PHYSICS = 64
    FRACTURE_GRAPHICS = 128
    DYNAMIC_SPLIT = 256
    DEFAULT_EXECUTION_FLAGS = 255


class Topology(Enum):
    TOPOLOGY_CLOSED_MANIFOLD = 0
    TOPOLOGY_OPEN_SELF_INTERSECTING = 1
    TOPOLOGY_UNKNOWN = 2


class hkcdFractureEngine(hkReferencedObject):
    pass

    def __repr__(self):
        return "<{class_name} >".format(**{
            "class_name": self.__class__.__name__,
        })
