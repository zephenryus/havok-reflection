from enum import Enum
from .hkClassEnumItem import hkClassEnumItem
from .hkCustomAttributes import hkCustomAttributes
from .common import any


class FlagValues(Enum):
    FLAGS_NONE = 0


class hkClassEnum(object):
    name: str
    items: hkClassEnumItem
    attributes: hkCustomAttributes
    flags: any

    def __init__(self, infile):
        self.name = str(infile)  # TYPE_CSTRING
        self.items = hkClassEnumItem(infile)  # TYPE_SIMPLEARRAY
        self.attributes = hkCustomAttributes(infile)  # TYPE_POINTER
        self.flags = any(infile)  # TYPE_FLAGS
