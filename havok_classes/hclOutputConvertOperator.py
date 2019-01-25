from .hclOperator import hclOperator
import struct
from .hclRuntimeConversionInfo import hclRuntimeConversionInfo


class hclOutputConvertOperator(hclOperator):
    userBufferIndex: int
    shadowBufferIndex: int
    conversionInfo: hclRuntimeConversionInfo

    def __init__(self, infile):
        self.userBufferIndex = struct.unpack('>I', infile.read(4))  # TYPE_UINT32:TYPE_VOID
        self.shadowBufferIndex = struct.unpack('>I', infile.read(4))  # TYPE_UINT32:TYPE_VOID
        self.conversionInfo = hclRuntimeConversionInfo(infile)  # TYPE_STRUCT:TYPE_VOID

    def __repr__(self):
        return "<{class_name} userBufferIndex={userBufferIndex}, shadowBufferIndex={shadowBufferIndex}, conversionInfo={conversionInfo}>".format(**{
            "class_name": self.__class__.__name__,
            "userBufferIndex": self.userBufferIndex,
            "shadowBufferIndex": self.shadowBufferIndex,
            "conversionInfo": self.conversionInfo,
        })
