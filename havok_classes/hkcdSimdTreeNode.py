from .hkcdFourAabb import hkcdFourAabb
from enum import Enum


class Flags(Enum):
    HAS_INTERNALS = 1
    HAS_LEAVES = 2
    HAS_NULLS = 4


class hkcdSimdTreeNode(hkcdFourAabb):
    data: int
