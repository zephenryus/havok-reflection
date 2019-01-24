from .hkpConstraintInstance import hkpConstraintInstance
from .hkpEntity import hkpEntity
from .hkpConstraintChainInstanceAction import hkpConstraintChainInstanceAction


class hkpConstraintChainInstance(hkpConstraintInstance):
    chainedEntities: hkpEntity
    action: hkpConstraintChainInstanceAction
    chainConnectedness: int
