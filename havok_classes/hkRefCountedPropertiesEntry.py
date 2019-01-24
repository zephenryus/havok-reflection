from .hkReferencedObject import hkReferencedObject


class hkRefCountedPropertiesEntry(object):
    object: hkReferencedObject
    key: int
    flags: int
