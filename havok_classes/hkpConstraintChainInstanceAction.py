from .hkpAction import hkpAction
from .hkpConstraintChainInstance import hkpConstraintChainInstance


class hkpConstraintChainInstanceAction(hkpAction):
    constraintInstance: any

    def __init__(self, infile):
        self.constraintInstance = any(infile)  # TYPE_POINTER:TYPE_STRUCT

    def __repr__(self):
        return "<{class_name} constraintInstance={constraintInstance}>".format(**{
            "class_name": self.__class__.__name__,
            "constraintInstance": self.constraintInstance,
        })
