from .hclOperatorSetupObject import hclOperatorSetupObject
from .hclSimClothSetupObject import hclSimClothSetupObject
from .hclBufferSetupObject import hclBufferSetupObject


class hclMoveFixedParticlesSetupObject(hclOperatorSetupObject):
    name: str
    simClothSetupObject: hclSimClothSetupObject
    displayBufferSetup: hclBufferSetupObject
