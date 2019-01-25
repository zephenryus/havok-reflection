from .hkReferencedObject import hkReferencedObject
from enum import Enum


class AccessFlags(Enum):
    ACCESS_INDICES = 1
    ACCESS_VERTEX_BUFFER = 2


class hkMeshShape(hkReferencedObject):
    pass

    def __repr__(self):
        return "<{class_name} >".format(**{
            "class_name": self.__class__.__name__,
        })
