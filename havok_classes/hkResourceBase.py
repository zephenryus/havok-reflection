from .hkReferencedObject import hkReferencedObject
from enum import Enum


class Type(Enum):
    TYPE_RESOURCE = 0
    TYPE_CONTAINER = 1


class hkResourceBase(hkReferencedObject):
    pass

    def __repr__(self):
        return "<{class_name} >".format(**{
            "class_name": self.__class__.__name__,
        })
