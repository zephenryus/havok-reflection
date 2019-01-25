from .hkcdFourAabb import hkcdFourAabb
from enum import Enum
import struct


class Flags(Enum):
    HAS_INTERNALS = 1
    HAS_LEAVES = 2
    HAS_NULLS = 4


class hkcdSimdTreeNode(hkcdFourAabb):
    data: int

    def __init__(self, infile):
        self.data = struct.unpack('>I', infile.read(4))
