from .hclOperatorSetupObject import hclOperatorSetupObject
from .hclSimClothSetupObject import hclSimClothSetupObject
import struct
from .hclConstraintSetSetupObject import hclConstraintSetSetupObject


class hclSimulateSetupObject(hclOperatorSetupObject):
    name: str
    simClothSetupObject: hclSimClothSetupObject
    numberOfSubsteps: int
    numberOfSolveIterations: int
    adaptConstraintStiffness: bool
    explicitConstraintOrder: bool
    constraintSetExecutionOrder: hclConstraintSetSetupObject

    def __init__(self, infile):
        self.name = struct.unpack('>s', infile.read(0))
        self.simClothSetupObject = hclSimClothSetupObject(infile)  # TYPE_POINTER
        self.numberOfSubsteps = struct.unpack('>I', infile.read(4))
        self.numberOfSolveIterations = struct.unpack('>I', infile.read(4))
        self.adaptConstraintStiffness = struct.unpack('>?', infile.read(1))
        self.explicitConstraintOrder = struct.unpack('>?', infile.read(1))
        self.constraintSetExecutionOrder = hclConstraintSetSetupObject(infile)  # TYPE_ARRAY
