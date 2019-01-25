from .hclOperatorSetupObject import hclOperatorSetupObject
from .hclSimClothSetupObject import hclSimClothSetupObject
from .hclBufferSetupObject import hclBufferSetupObject


class hclMoveFixedParticlesSetupObject(hclOperatorSetupObject):
    name: str
    simClothSetupObject: any
    displayBufferSetup: any

    def __init__(self, infile):
        self.name = struct.unpack('>s', infile.read(0))  # TYPE_STRINGPTR:TYPE_VOID
        self.simClothSetupObject = any(infile)  # TYPE_POINTER:TYPE_STRUCT
        self.displayBufferSetup = any(infile)  # TYPE_POINTER:TYPE_STRUCT

    def __repr__(self):
        return "<{class_name} name=\"{name}\", simClothSetupObject={simClothSetupObject}, displayBufferSetup={displayBufferSetup}>".format(**{
            "class_name": self.__class__.__name__,
            "name": self.name,
            "simClothSetupObject": self.simClothSetupObject,
            "displayBufferSetup": self.displayBufferSetup,
        })
