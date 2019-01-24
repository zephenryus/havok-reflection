from .hkpBvTreeShape import hkpBvTreeShape
from enum import Enum
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
