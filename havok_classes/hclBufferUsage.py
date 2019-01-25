from enum import Enum
import struct


class Component(Enum):
    COMPONENT_POSITION = 0
    COMPONENT_NORMAL = 1
    COMPONENT_TANGENT = 2
    COMPONENT_BITANGENT = 3


class InternalFlags(Enum):
    USAGE_NONE = 0
    USAGE_READ = 1
    USAGE_WRITE = 2
    USAGE_FULL_WRITE = 4
    USAGE_READ_BEFORE_WRITE = 8


class hclBufferUsage(object):
    perComponentFlags: int
    trianglesRead: bool

    def __init__(self, infile):
        self.perComponentFlags = struct.unpack('>B', infile.read(1))
        self.trianglesRead = struct.unpack('>?', infile.read(1))
