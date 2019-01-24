from .hkReferencedObject import hkReferencedObject
from .hkcdDynamicTreeDefaultTree48Storage import hkcdDynamicTreeDefaultTree48Storage


class hkcdDynamicAabbTree(hkReferencedObject):
    shouldDeleteTree: bool
    treePtr: hkcdDynamicTreeDefaultTree48Storage
