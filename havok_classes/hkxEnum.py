from .hkReferencedObject import hkReferencedObject
from typing import List
from .common import get_array
from .hkxEnumItem import hkxEnumItem


class hkxEnum(hkReferencedObject):
    items: List[hkxEnumItem]

    def __init__(self, infile):
        self.items = get_array(infile, hkxEnumItem, 0)  # TYPE_ARRAY:TYPE_STRUCT

    def __repr__(self):
        return "<{class_name} items=[{items}]>".format(**{
            "class_name": self.__class__.__name__,
            "items": self.items,
        })
