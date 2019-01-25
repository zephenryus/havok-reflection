from enum import Enum
from typing import List
from .common import get_array
from .hkRefCountedPropertiesEntry import hkRefCountedPropertiesEntry


class ReferenceCountHandling(Enum):
    REFERENCE_COUNT_INCREMENT = 0
    REFERENCE_COUNT_IGNORE = 1


class hkRefCountedProperties(object):
    entries: List[hkRefCountedPropertiesEntry]

    def __init__(self, infile):
        self.entries = get_array(infile, hkRefCountedPropertiesEntry, 0)  # TYPE_ARRAY:TYPE_STRUCT

    def __repr__(self):
        return "<{class_name} entries=[{entries}]>".format(**{
            "class_name": self.__class__.__name__,
            "entries": self.entries,
        })
