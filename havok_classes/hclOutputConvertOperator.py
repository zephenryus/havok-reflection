from .hclOperator import hclOperator
from .hclRuntimeConversionInfo import hclRuntimeConversionInfo


class hclOutputConvertOperator(hclOperator):
	userBufferIndex: int
	shadowBufferIndex: int
	conversionInfo: hclRuntimeConversionInfo
