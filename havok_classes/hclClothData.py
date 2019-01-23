from .hkReferencedObject import hkReferencedObject
from .hclSimClothData import hclSimClothData
from .hclBufferDefinition import hclBufferDefinition
from .hclTransformSetDefinition import hclTransformSetDefinition
from .hclOperator import hclOperator
from .hclClothState import hclClothState
from .hclAction import hclAction


class hclClothData(hkReferencedObject):
	name: any
	simClothDatas: hclSimClothData
	bufferDefinitions: hclBufferDefinition
	transformSetDefinitions: hclTransformSetDefinition
	operators: hclOperator
	clothStateDatas: hclClothState
	actions: hclAction
	targetPlatform: any
