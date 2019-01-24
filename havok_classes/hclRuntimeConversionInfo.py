from enum import Enum
from .hclRuntimeConversionInfoSlotConversion import hclRuntimeConversionInfoSlotConversion
from .hclRuntimeConversionInfoElementConversion import hclRuntimeConversionInfoElementConversion


class VectorConversion(Enum):
    VC_FLOAT4 = 0
    VC_FLOAT3 = 1
    VC_BYTE4 = 2
    VC_SHORT3 = 3
    VC_HFLOAT3 = 4
    VC_CUSTOM_A = 20
    VC_CUSTOM_B = 21
    VC_CUSTOM_C = 22
    VC_CUSTOM_D = 23
    VC_CUSTOM_E = 24
    VC_NONE = 250


class hclRuntimeConversionInfo(object):
    slotConversions: hclRuntimeConversionInfoSlotConversion
    elementConversions: hclRuntimeConversionInfoElementConversion
    numSlotsConverted: int
    numElementsConverted: int
