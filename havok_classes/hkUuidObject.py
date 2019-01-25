from .hkReferencedObject import hkReferencedObject
from .hkUuid import hkUuid


class hkUuidObject(hkReferencedObject):
    uuid: hkUuid

    def __init__(self, infile):
        self.uuid = hkUuid(infile)  # TYPE_STRUCT
