from .hkcdStaticTreeDynamicStorage32 import hkcdStaticTreeDynamicStorage32
from .hkAabb import hkAabb


class hkcdStaticTreeTreehkcdStaticTreeDynamicStorage32(hkcdStaticTreeDynamicStorage32):
    domain: hkAabb

    def __init__(self, infile):
        self.domain = hkAabb(infile)  # TYPE_STRUCT
