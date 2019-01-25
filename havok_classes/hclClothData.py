from .hkReferencedObject import hkReferencedObject
from enum import Enum
from typing import List
from .common import get_array
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
    simClothDatas: List[hclSimClothData]
    bufferDefinitions: List[hclBufferDefinition]
    transformSetDefinitions: List[hclTransformSetDefinition]
    operators: List[hclOperator]
    clothStateDatas: List[hclClothState]
    actions: List[hclAction]
    targetPlatform: Platform

    def __init__(self, infile):
        self.name = struct.unpack('>s', infile.read(0))  # TYPE_STRINGPTR:TYPE_VOID
        self.simClothDatas = get_array(infile, hclSimClothData, 0)  # TYPE_ARRAY:TYPE_POINTER
        self.bufferDefinitions = get_array(infile, hclBufferDefinition, 0)  # TYPE_ARRAY:TYPE_POINTER
        self.transformSetDefinitions = get_array(infile, hclTransformSetDefinition, 0)  # TYPE_ARRAY:TYPE_POINTER
        self.operators = get_array(infile, hclOperator, 0)  # TYPE_ARRAY:TYPE_POINTER
        self.clothStateDatas = get_array(infile, hclClothState, 0)  # TYPE_ARRAY:TYPE_POINTER
        self.actions = get_array(infile, hclAction, 0)  # TYPE_ARRAY:TYPE_POINTER
        self.targetPlatform = Platform(infile)  # TYPE_ENUM:TYPE_UINT32

    def __repr__(self):
        return "<{class_name} name=\"{name}\", simClothDatas=[{simClothDatas}], bufferDefinitions=[{bufferDefinitions}], transformSetDefinitions=[{transformSetDefinitions}], operators=[{operators}], clothStateDatas=[{clothStateDatas}], actions=[{actions}], targetPlatform={targetPlatform}>".format(**{
            "class_name": self.__class__.__name__,
            "name": self.name,
            "simClothDatas": self.simClothDatas,
            "bufferDefinitions": self.bufferDefinitions,
            "transformSetDefinitions": self.transformSetDefinitions,
            "operators": self.operators,
            "clothStateDatas": self.clothStateDatas,
            "actions": self.actions,
            "targetPlatform": self.targetPlatform,
        })
