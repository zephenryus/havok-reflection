from .hclOperatorSetupObject import hclOperatorSetupObject
from .hclSimClothSetupObject import hclSimClothSetupObject
from .hclBufferSetupObject import hclBufferSetupObject


class hclMoveFixedParticlesSetupObject(hclOperatorSetupObject):
    name: str
    simClothSetupObject: hclSimClothSetupObject
    displayBufferSetup: hclBufferSetupObject

    def __init__(self, infile):
        self.name = struct.unpack('>s', infile.read(0))
        self.simClothSetupObject = hclSimClothSetupObject(infile)  # TYPE_POINTER
        self.displayBufferSetup = hclBufferSetupObject(infile)  # TYPE_POINTER
