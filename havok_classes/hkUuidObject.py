from .hkReferencedObject import hkReferencedObject
from .hkUuid import hkUuid


class hkUuidObject(hkReferencedObject):
    uuid: hkUuid

    def __init__(self, infile):
        self.uuid = hkUuid(infile)  # TYPE_STRUCT:TYPE_VOID

    def __repr__(self):
        return "<{class_name} uuid={uuid}>".format(**{
            "class_name": self.__class__.__name__,
            "uuid": self.uuid,
        })
