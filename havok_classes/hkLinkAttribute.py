from enum import Enum
from .enums import Link


class Link(Enum):
    NONE = 0
    DIRECT_LINK = 1
    CHILD = 2
    MESH = 3
    PARENT_NAME = 4
    IMGSELECT = 5
    NODE_UUID = 6


class hkLinkAttribute(object):
    type: Link

    def __init__(self, infile):
        self.type = Link(infile)  # TYPE_ENUM
