from enum import Enum
from .hclRuntimeConversionInfoSlotConversion import hclRuntimeConversionInfoSlotConversion
from .hclRuntimeConversionInfoElementConversion import hclRuntimeConversionInfoElementConversion
import struct


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

    def __init__(self, infile):
        self.slotConversions = hclRuntimeConversionInfoSlotConversion(infile)  # TYPE_STRUCT:TYPE_VOID
        self.elementConversions = hclRuntimeConversionInfoElementConversion(infile)  # TYPE_STRUCT:TYPE_VOID
        self.numSlotsConverted = struct.unpack('>B', infile.read(1))  # TYPE_UINT8:TYPE_VOID
        self.numElementsConverted = struct.unpack('>B', infile.read(1))  # TYPE_UINT8:TYPE_VOID

    def __repr__(self):
        return "<{class_name} slotConversions={slotConversions}, elementConversions={elementConversions}, numSlotsConverted={numSlotsConverted}, numElementsConverted={numElementsConverted}>".format(**{
            "class_name": self.__class__.__name__,
            "slotConversions": self.slotConversions,
            "elementConversions": self.elementConversions,
            "numSlotsConverted": self.numSlotsConverted,
            "numElementsConverted": self.numElementsConverted,
        })
