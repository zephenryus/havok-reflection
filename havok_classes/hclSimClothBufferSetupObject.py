from .hclBufferSetupObject import hclBufferSetupObject
from .hclSimClothSetupObject import hclSimClothSetupObject


class hclSimClothBufferSetupObject(hclBufferSetupObject):
	type: any
	name: any
	simClothSetupObject: hclSimClothSetupObject
