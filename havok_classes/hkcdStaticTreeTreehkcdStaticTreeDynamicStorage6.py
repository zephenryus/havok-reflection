from .hkcdStaticTreeDynamicStorage6 import hkcdStaticTreeDynamicStorage6
from .hkAabb import hkAabb


class hkcdStaticTreeTreehkcdStaticTreeDynamicStorage6(hkcdStaticTreeDynamicStorage6):
    domain: hkAabb

    def __init__(self, infile):
        self.domain = hkAabb(infile)  # TYPE_STRUCT
