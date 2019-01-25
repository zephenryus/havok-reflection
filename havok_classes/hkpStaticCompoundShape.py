from .hkpBvTreeShape import hkpBvTreeShape
from enum import Enum
import struct
from .hkpStaticCompoundShapeInstance import hkpStaticCompoundShapeInstance
from .common import any
from .hkpShapeKeyTable import hkpShapeKeyTable
from .hkcdStaticTreeDefaultTreeStorage6 import hkcdStaticTreeDefaultTreeStorage6


class Config(Enum):
    NUM_BYTES_FOR_TREE = 48


class hkpStaticCompoundShape(hkpBvTreeShape):
    numBitsForChildShapeKey: int
    referencePolicy: int
    childShapeKeyMask: int
    instances: hkpStaticCompoundShapeInstance
    instanceExtraInfos: any
    disabledLargeShapeKeyTable: hkpShapeKeyTable
    tree: hkcdStaticTreeDefaultTreeStorage6

    def __init__(self, infile):
        self.numBitsForChildShapeKey = struct.unpack('>b', infile.read(1))
        self.referencePolicy = struct.unpack('>b', infile.read(1))
        self.childShapeKeyMask = struct.unpack('>I', infile.read(4))
        self.instances = hkpStaticCompoundShapeInstance(infile)  # TYPE_ARRAY
        self.instanceExtraInfos = any(infile)  # TYPE_ARRAY
        self.disabledLargeShapeKeyTable = hkpShapeKeyTable(infile)  # TYPE_STRUCT
        self.tree = hkcdStaticTreeDefaultTreeStorage6(infile)  # TYPE_STRUCT
