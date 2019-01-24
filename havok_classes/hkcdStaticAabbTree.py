from .hkReferencedObject import hkReferencedObject
from .hkcdStaticTreeDefaultTreeStorage6 import hkcdStaticTreeDefaultTreeStorage6


class hkcdStaticAabbTree(hkReferencedObject):
    shouldDeleteTree: bool
    treePtr: hkcdStaticTreeDefaultTreeStorage6
