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
        self.type = Link(infile)  # TYPE_ENUM:TYPE_INT8

    def __repr__(self):
        return "<{class_name} type={type}>".format(**{
            "class_name": self.__class__.__name__,
            "type": self.type,
        })
