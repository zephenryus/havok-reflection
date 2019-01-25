from .hkReferencedObject import hkReferencedObject
from enum import Enum
from .hkpMoppCodeCodeInfo import hkpMoppCodeCodeInfo
from typing import List
from .common import get_array
from .enums import BuildType


class BuildType(Enum):
    BUILT_WITH_CHUNK_SUBDIVISION = 0
    BUILT_WITHOUT_CHUNK_SUBDIVISION = 1
    BUILD_NOT_SET = 2


class hkpMoppCode(hkReferencedObject):
    info: hkpMoppCodeCodeInfo
    data: List[int]
    buildType: BuildType

    def __init__(self, infile):
        self.info = hkpMoppCodeCodeInfo(infile)  # TYPE_STRUCT:TYPE_VOID
        self.data = get_array(infile, int, 1)  # TYPE_ARRAY:TYPE_UINT8
        self.buildType = BuildType(infile)  # TYPE_ENUM:TYPE_INT8

    def __repr__(self):
        return "<{class_name} info={info}, data=[{data}], buildType={buildType}>".format(**{
            "class_name": self.__class__.__name__,
            "info": self.info,
            "data": self.data,
            "buildType": self.buildType,
        })
