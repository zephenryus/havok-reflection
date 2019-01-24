from .hkReferencedObject import hkReferencedObject
from enum import Enum


class MaxConstraintSetSize(Enum):
    MAX_CONSTRAINT_SET_SIZE = 128


class hclConstraintSet(hkReferencedObject):
    name: str
    type: enumerate
