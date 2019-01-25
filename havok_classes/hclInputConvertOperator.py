from .hclOperator import hclOperator
import struct
from .hclRuntimeConversionInfo import hclRuntimeConversionInfo


class hclInputConvertOperator(hclOperator):
    userBufferIndex: int
    shadowBufferIndex: int
    conversionInfo: hclRuntimeConversionInfo

    def __init__(self, infile):
        self.userBufferIndex = struct.unpack('>I', infile.read(4))
        self.shadowBufferIndex = struct.unpack('>I', infile.read(4))
        self.conversionInfo = hclRuntimeConversionInfo(infile)  # TYPE_STRUCT
