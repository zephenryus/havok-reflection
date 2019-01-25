from .hkpAction import hkpAction
from .hkpConstraintChainInstance import hkpConstraintChainInstance


class hkpConstraintChainInstanceAction(hkpAction):
    constraintInstance: hkpConstraintChainInstance

    def __init__(self, infile):
        self.constraintInstance = hkpConstraintChainInstance(infile)  # TYPE_POINTER
