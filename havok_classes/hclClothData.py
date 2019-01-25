from .hkReferencedObject import hkReferencedObject
from enum import Enum
from .hclSimClothData import hclSimClothData
from .hclBufferDefinition import hclBufferDefinition
from .hclTransformSetDefinition import hclTransformSetDefinition
from .hclOperator import hclOperator
from .hclClothState import hclClothState
from .hclAction import hclAction
from .enums import Platform


class Platform(Enum):
    HCL_PLATFORM_INVALID = 0
    HCL_PLATFORM_WIN32 = 1
    HCL_PLATFORM_X64 = 2
    HCL_PLATFORM_MACPPC = 4
    HCL_PLATFORM_IOS = 8
    HCL_PLATFORM_MAC386 = 16
    HCL_PLATFORM_PS3 = 32
    HCL_PLATFORM_XBOX360 = 64
    HCL_PLATFORM_WII = 128
    HCL_PLATFORM_LRB = 256
    HCL_PLATFORM_LINUX = 512
    HCL_PLATFORM_PSVITA = 1024
    HCL_PLATFORM_ANDROID = 2048
    HCL_PLATFORM_CTR = 4096
    HCL_PLATFORM_WIIU = 8192
    HCL_PLATFORM_PS4 = 16384
    HCL_PLATFORM_XBOXONE = 32768
    HCL_PLATFORM_MAC64 = 65536
    HCL_PLATFORM_NX = 131072


class hclClothData(hkReferencedObject):
    name: str
    simClothDatas: hclSimClothData
    bufferDefinitions: hclBufferDefinition
    transformSetDefinitions: hclTransformSetDefinition
    operators: hclOperator
    clothStateDatas: hclClothState
    actions: hclAction
    targetPlatform: Platform

    def __init__(self, infile):
        self.name = struct.unpack('>s', infile.read(0))
        self.simClothDatas = hclSimClothData(infile)  # TYPE_ARRAY
        self.bufferDefinitions = hclBufferDefinition(infile)  # TYPE_ARRAY
        self.transformSetDefinitions = hclTransformSetDefinition(infile)  # TYPE_ARRAY
        self.operators = hclOperator(infile)  # TYPE_ARRAY
        self.clothStateDatas = hclClothState(infile)  # TYPE_ARRAY
        self.actions = hclAction(infile)  # TYPE_ARRAY
        self.targetPlatform = Platform(infile)  # TYPE_ENUM
