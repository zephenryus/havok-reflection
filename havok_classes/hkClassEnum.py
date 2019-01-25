from enum import Enum
from .hkClassEnumItem import hkClassEnumItem
from .hkCustomAttributes import hkCustomAttributes


class FlagValues(Enum):
    FLAGS_NONE = 0


class hkClassEnum(object):
    name: str
    items: any
    attributes: any
    flags: any

    def __init__(self, infile):
        self.name = str(infile)  # TYPE_CSTRING:TYPE_VOID
        self.items = any(infile)  # TYPE_SIMPLEARRAY:TYPE_STRUCT
        self.attributes = any(infile)  # TYPE_POINTER:TYPE_STRUCT
        self.flags = any(infile)  # TYPE_FLAGS:TYPE_UINT32

    def __repr__(self):
        return "<{class_name} name=\"{name}\", items={items}, attributes={attributes}, flags={flags}>".format(**{
            "class_name": self.__class__.__name__,
            "name": self.name,
            "items": self.items,
            "attributes": self.attributes,
            "flags": self.flags,
        })
