from .hclOperatorSetupObject import hclOperatorSetupObject
from .hclSimClothSetupObject import hclSimClothSetupObject
import struct
from typing import List
from .common import get_array
from .hclConstraintSetSetupObject import hclConstraintSetSetupObject


class hclSimulateSetupObject(hclOperatorSetupObject):
    name: str
    simClothSetupObject: any
    numberOfSubsteps: int
    numberOfSolveIterations: int
    adaptConstraintStiffness: bool
    explicitConstraintOrder: bool
    constraintSetExecutionOrder: List[hclConstraintSetSetupObject]

    def __init__(self, infile):
        self.name = struct.unpack('>s', infile.read(0))  # TYPE_STRINGPTR:TYPE_VOID
        self.simClothSetupObject = any(infile)  # TYPE_POINTER:TYPE_STRUCT
        self.numberOfSubsteps = struct.unpack('>I', infile.read(4))  # TYPE_UINT32:TYPE_VOID
        self.numberOfSolveIterations = struct.unpack('>I', infile.read(4))  # TYPE_UINT32:TYPE_VOID
        self.adaptConstraintStiffness = struct.unpack('>?', infile.read(1))  # TYPE_BOOL:TYPE_VOID
        self.explicitConstraintOrder = struct.unpack('>?', infile.read(1))  # TYPE_BOOL:TYPE_VOID
        self.constraintSetExecutionOrder = get_array(infile, hclConstraintSetSetupObject, 0)  # TYPE_ARRAY:TYPE_POINTER

    def __repr__(self):
        return "<{class_name} name=\"{name}\", simClothSetupObject={simClothSetupObject}, numberOfSubsteps={numberOfSubsteps}, numberOfSolveIterations={numberOfSolveIterations}, adaptConstraintStiffness={adaptConstraintStiffness}, explicitConstraintOrder={explicitConstraintOrder}, constraintSetExecutionOrder=[{constraintSetExecutionOrder}]>".format(**{
            "class_name": self.__class__.__name__,
            "name": self.name,
            "simClothSetupObject": self.simClothSetupObject,
            "numberOfSubsteps": self.numberOfSubsteps,
            "numberOfSolveIterations": self.numberOfSolveIterations,
            "adaptConstraintStiffness": self.adaptConstraintStiffness,
            "explicitConstraintOrder": self.explicitConstraintOrder,
            "constraintSetExecutionOrder": self.constraintSetExecutionOrder,
        })
