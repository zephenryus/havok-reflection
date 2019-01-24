from .hkReferencedObject import hkReferencedObject
from enum import Enum
from .hkpMoppCodeCodeInfo import hkpMoppCodeCodeInfo
from .common import any
from .enums import BuildType


class BuildType(Enum):
    BUILT_WITH_CHUNK_SUBDIVISION = 0
    BUILT_WITHOUT_CHUNK_SUBDIVISION = 1
    BUILD_NOT_SET = 2


class hkpMoppCode(hkReferencedObject):
    info: hkpMoppCodeCodeInfo
    data: any
    buildType: BuildType
