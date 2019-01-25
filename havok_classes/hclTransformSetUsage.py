from enum import Enum
import struct
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
    perComponentTransformTrackers: hclTransformSetUsageTransformTracker

    def __init__(self, infile):
        self.perComponentFlags = struct.unpack('>B', infile.read(1))
        self.perComponentTransformTrackers = hclTransformSetUsageTransformTracker(infile)  # TYPE_ARRAY
