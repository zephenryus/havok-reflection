from .hkpBvTreeShape import hkpBvTreeShape
from enum import Enum
import struct
from typing import List
from .common import get_array
from .hkpStaticCompoundShapeInstance import hkpStaticCompoundShapeInstance
from .hkpShapeKeyTable import hkpShapeKeyTable
from .hkcdStaticTreeDefaultTreeStorage6 import hkcdStaticTreeDefaultTreeStorage6


class Config(Enum):
    NUM_BYTES_FOR_TREE = 48


class hkpStaticCompoundShape(hkpBvTreeShape):
    numBitsForChildShapeKey: int
    referencePolicy: int
    childShapeKeyMask: int
    instances: List[hkpStaticCompoundShapeInstance]
    instanceExtraInfos: List[int]
    disabledLargeShapeKeyTable: hkpShapeKeyTable
    tree: hkcdStaticTreeDefaultTreeStorage6

    def __init__(self, infile):
        self.numBitsForChildShapeKey = struct.unpack('>b', infile.read(1))  # TYPE_INT8:TYPE_VOID
        self.referencePolicy = struct.unpack('>b', infile.read(1))  # TYPE_INT8:TYPE_VOID
        self.childShapeKeyMask = struct.unpack('>I', infile.read(4))  # TYPE_UINT32:TYPE_VOID
        self.instances = get_array(infile, hkpStaticCompoundShapeInstance, 0)  # TYPE_ARRAY:TYPE_STRUCT
        self.instanceExtraInfos = get_array(infile, int, 2)  # TYPE_ARRAY:TYPE_UINT16
        self.disabledLargeShapeKeyTable = hkpShapeKeyTable(infile)  # TYPE_STRUCT:TYPE_VOID
        self.tree = hkcdStaticTreeDefaultTreeStorage6(infile)  # TYPE_STRUCT:TYPE_VOID

    def __repr__(self):
        return "<{class_name} numBitsForChildShapeKey={numBitsForChildShapeKey}, referencePolicy={referencePolicy}, childShapeKeyMask={childShapeKeyMask}, instances=[{instances}], instanceExtraInfos=[{instanceExtraInfos}], disabledLargeShapeKeyTable={disabledLargeShapeKeyTable}, tree={tree}>".format(**{
            "class_name": self.__class__.__name__,
            "numBitsForChildShapeKey": self.numBitsForChildShapeKey,
            "referencePolicy": self.referencePolicy,
            "childShapeKeyMask": self.childShapeKeyMask,
            "instances": self.instances,
            "instanceExtraInfos": self.instanceExtraInfos,
            "disabledLargeShapeKeyTable": self.disabledLargeShapeKeyTable,
            "tree": self.tree,
        })
