from .hclOperator import hclOperator
from .hclRuntimeConversionInfo import hclRuntimeConversionInfo


class hclInputConvertOperator(hclOperator):
    userBufferIndex: int
    shadowBufferIndex: int
    conversionInfo: hclRuntimeConversionInfo
