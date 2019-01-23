from .hclOperatorSetupObject import hclOperatorSetupObject
from .hclSimClothSetupObject import hclSimClothSetupObject
from .hclBufferSetupObject import hclBufferSetupObject


class hclMoveFixedParticlesSetupObject(hclOperatorSetupObject):
	name: any
	simClothSetupObject: hclSimClothSetupObject
	displayBufferSetup: hclBufferSetupObject
