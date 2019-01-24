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
