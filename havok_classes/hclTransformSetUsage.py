from enum import Enum
import struct
from typing import List
from .common import get_array
from .hclTransformSetUsageTransformTracker import hclTransformSetUsageTransformTracker


class Component(Enum):
    COMPONENT_TRANSFORM = 0
    COMPONENT_INVTRANSPOSE = 1
    NUM_COMPONENTS = 2


class InternalFlags(Enum):
    USAGE_NONE = 0
    USAGE_READ = 1
    USAGE_WRITE = 2
    USAGE_FULL_WRITE = 4
    USAGE_READ_BEFORE_WRITE = 8


class hclTransformSetUsage(object):
    perComponentFlags: int
    perComponentTransformTrackers: List[hclTransformSetUsageTransformTracker]

    def __init__(self, infile):
        self.perComponentFlags = struct.unpack('>B', infile.read(1))  # TYPE_UINT8:TYPE_VOID
        self.perComponentTransformTrackers = get_array(infile, hclTransformSetUsageTransformTracker, 0)  # TYPE_ARRAY:TYPE_STRUCT

    def __repr__(self):
        return "<{class_name} perComponentFlags={perComponentFlags}, perComponentTransformTrackers=[{perComponentTransformTrackers}]>".format(**{
            "class_name": self.__class__.__name__,
            "perComponentFlags": self.perComponentFlags,
            "perComponentTransformTrackers": self.perComponentTransformTrackers,
        })
