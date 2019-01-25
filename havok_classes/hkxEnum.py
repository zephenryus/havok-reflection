from .hkReferencedObject import hkReferencedObject
from .hkxEnumItem import hkxEnumItem


class hkxEnum(hkReferencedObject):
    items: hkxEnumItem

    def __init__(self, infile):
        self.items = hkxEnumItem(infile)  # TYPE_ARRAY
