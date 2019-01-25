from .hkpAction import hkpAction
from .hkpEntity import hkpEntity


class hkpBinaryAction(hkpAction):
    entityA: any
    entityB: any

    def __init__(self, infile):
        self.entityA = any(infile)  # TYPE_POINTER:TYPE_STRUCT
        self.entityB = any(infile)  # TYPE_POINTER:TYPE_STRUCT

    def __repr__(self):
        return "<{class_name} entityA={entityA}, entityB={entityB}>".format(**{
            "class_name": self.__class__.__name__,
            "entityA": self.entityA,
            "entityB": self.entityB,
        })
